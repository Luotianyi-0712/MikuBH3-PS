from game_server.net.gateway import Gateway

class GameServer:
    def main(self, ServerIp, GameServerPort):
        Gateway(ServerIp, GameServerPort)
