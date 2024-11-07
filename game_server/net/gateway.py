from game_server.config.log import Info
from game_server.net.session import Session
import asyncio

class Gateway:
    def __init__(self, server_ip, game_server_port) -> None:
        self.server_ip = server_ip
        self.game_server_port = game_server_port
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        try:
            self.loop.run_until_complete(self.start_server())
        finally:
            self.loop.run_until_complete(self.loop.shutdown_asyncgens())
            self.loop.close()

    async def start_server(self):
        session = Session()
        server = await asyncio.start_server(session.handle_connection, self.server_ip, self.game_server_port)
        Info("Gateway listening...")
        async with server:
            await server.serve_forever()

    

