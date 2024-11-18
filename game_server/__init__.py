from game_server.net.gateway import Gateway
from game_server.game.chat.command_handler import handler

class GameServer:
    def main(self, ServerIp, GameServerPort):
        handler.load_commands()
        Gateway(ServerIp, GameServerPort)
