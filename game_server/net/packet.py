import struct
from game_server.protocol.cmd_id import CmdID

class Packet:
    def __init__(self, buf: bytes):
        self.raw = buf
        self.head_magic = buf[:4] 
        self.user_id = struct.unpack('>I', buf[12:16])[0]
        self.cmd_id = struct.unpack('>I', buf[24:28])[0]


        self.header_len = struct.unpack('>H', buf[28:30])[0] 
        self.body_len = struct.unpack('>I', buf[30:34])[0] 
        self.body = buf[34 + self.header_len:34 + self.header_len + self.body_len]
        self.tail_magic = buf[-4:]


    @staticmethod
    def send_packet(body):
        cmdid = CmdID[body.__class__.__name__]
        data = body.SerializeToString()  

        buf = bytearray(38 + len(data))

        struct.pack_into('>I', buf, 0, 0x01234567)       
        struct.pack_into('>H', buf, 4, 1)
        struct.pack_into('>H', buf, 6, 0)
        struct.pack_into('>I', buf, 8, 0)
        struct.pack_into('>I', buf, 12, 0)
        struct.pack_into('>I', buf, 16, 0)
        struct.pack_into('>I', buf, 20, 0)
        struct.pack_into('>I', buf, 24, cmdid)
        struct.pack_into('>H', buf, 28, 0)
        struct.pack_into('>I', buf, 30, len(data))

        buf[34:34 + len(data)] = data

        struct.pack_into('>I', buf, 34 + len(data), 0x89ABCDEF)


        return Packet(bytes(buf))