from utils.logger import Error, Info
from game_server.net.cmd_id import CmdID
from game_server.net.packet import Packet
from lib import proto as protos
import traceback
import betterproto
import importlib
import threading
import asyncio
from game_server.game.player import Player


class Session:
    player: Player

    def __init__(self) -> None:
        self.writer = None
        self.pending_notifies = []
        asyncio.create_task(self.keep_alive_loop())

    async def keep_alive_loop(self):
        while self.writer is None:
            await asyncio.sleep(1)
        while True:
            if self.writer.is_closing():
                break
            try:
                await self.send(Packet.send_packet(protos.KeepAliveNotify()))
            except Exception as ex:
                Error(f"Error in KeepAliveLoop: {ex}")
                break

            await asyncio.sleep(3)

    async def handle_connection(self, reader, writer):
        self.writer = writer
        addr = writer.get_extra_info("peername")
        Info(f"Accepted connection from {addr}")

        prefix = bytes([0x01, 0x23, 0x45, 0x67])
        suffix = bytes([0x89, 0xAB, 0xCD, 0xEF])

        try:
            while True:
                data = await reader.read(1 << 16)
                if not data:
                    break

                packets = []
                message = memoryview(data)

                offset = 0
                while offset < len(message):
                    segment = message[offset:].tobytes()
                    start = segment.find(prefix)

                    if start == -1:
                        break

                    end = segment.find(suffix, start)
                    if end == -1:
                        break

                    end += len(suffix)
                    packets.append(segment[start:end])
                    offset += end

                for packet in packets:
                    if self.is_valid_packet(packet):
                        processed_packet = Packet(packet)
                        await self.process_packet(processed_packet)
                    else:
                        Error(f"Invalid packet received: {packet.hex().upper()}")

        except Exception as e:
            Error(f"Exception in processing TCP: {e}")

        finally:
            writer.close()
            await writer.wait_closed()
            Info("Disconnected from protocol")

    def create_packet(self, proto_message: betterproto.Message) -> Packet:
        return Packet.send_packet(proto_message)

    def is_valid_packet(self, data: bytes) -> bool:
        hex_string = data.hex().upper()
        return hex_string.startswith("01234567") and hex_string.endswith("89ABCDEF")

    def pending_notify(self, proto_message: betterproto.Message):
        packet = Packet.send_packet(proto_message)
        self.pending_notifies.append(packet)

    def send_pending_notifies_in_thread(self):
        thread = threading.Thread(target=self._run_send_pending_notifies)
        thread.start()

    def _run_send_pending_notifies(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self._send_pending_notifies())
        loop.close()

    async def _send_pending_notifies(self):
        for packet in self.pending_notifies:
            await self.send(packet)
        self.pending_notifies.clear()

    async def process_packet(self, packet: Packet):
        if packet.cmd_id not in CmdID._value2member_map_:
            Error(f"CmdId {packet.cmd_id} not recognized!")
            return
        request_name = CmdID(packet.cmd_id).name
        if request_name == "KeepAliveNotify":
            return  # await self.send(packet.send_packet(protos.KeepAliveNotify()))
        try:
            try:
                req: betterproto.Message = getattr(protos, request_name)()
                req.parse(packet.body)
            except Exception:
                req = betterproto.Message()

            try:
                Info(f"RECV packet: {request_name} ({packet.cmd_id})")
                handle_module = importlib.import_module(
                    f"game_server.packet.handlers.{request_name}"
                )
                handle_function = handle_module.handle
                handle_result = await handle_function(self, req)
                if not handle_result:
                    return
                await self.send(packet.send_packet(handle_result))
                self.send_pending_notifies_in_thread()
            except ModuleNotFoundError:
                Error(f"Unhandled request {request_name}")
                return
            except Exception as e:
                Error(f"Handler {request_name} returned error: {e}")
                traceback.print_exc()
                return
        except Exception:
            Error("Packet processing failed. Traceback: ")
            traceback.print_exc()
            return

    async def send(self, packet: Packet):
        if packet.cmd_id not in CmdID._value2member_map_:
            Error(f"CmdId {packet.cmd_id} not recognized!")
            return
        packet_name = CmdID(packet.cmd_id).name
        try:
            self.writer.write(packet.raw)
            await self.writer.drain()
            Info(f"Sent packet: {packet_name} ({packet.cmd_id})")
        except Exception as ex:
            Error(f"Failed to send {packet_name}: {ex}")
            traceback.print_exc()
