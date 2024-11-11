import betterproto
from game_server.net.session import Session
from lib.proto import GetGodWarLobbyReq,GetGodWarLobbyRsp

async def handle(session: Session, msg: GetGodWarLobbyReq) -> betterproto.Message:
    return GetGodWarLobbyRsp(
        retcode=0,
        god_war_id=1,
        lobby_id=2
    )
