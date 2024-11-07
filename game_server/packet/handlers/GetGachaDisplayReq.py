import betterproto
from game_server.net.session import Session
from lib.proto import GetGachaDisplayReq, GetGachaDisplayRsp

async def handle(session: Session, msg: GetGachaDisplayReq) -> betterproto.Message:
    return GetGachaDisplayRsp(retcode=0)
