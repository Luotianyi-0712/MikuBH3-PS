import betterproto
from game_server.net.session import Session
from lib.proto import MassiveWarGetActivityReq, MassiveWarGetActivityRsp

async def handle(session: Session, msg: MassiveWarGetActivityReq) -> betterproto.Message:
    return MassiveWarGetActivityRsp(retcode=0)
