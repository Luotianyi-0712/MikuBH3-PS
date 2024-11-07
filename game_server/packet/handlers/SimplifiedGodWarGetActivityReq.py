import betterproto
from game_server.net.session import Session
from lib.proto import SimplifiedGodWarGetActivityReq,SimplifiedGodWarGetActivityRsp

async def handle(session: Session, msg: SimplifiedGodWarGetActivityReq) -> betterproto.Message:
    return SimplifiedGodWarGetActivityRsp(retcode=0)
