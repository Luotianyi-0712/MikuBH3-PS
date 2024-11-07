import betterproto
from game_server.net.session import Session
from lib.proto import GetNewbieActivityReq, GetNewbieActivityRsp

async def handle(session: Session, msg: GetNewbieActivityReq) -> betterproto.Message:
    return GetNewbieActivityRsp(retcode=0)
