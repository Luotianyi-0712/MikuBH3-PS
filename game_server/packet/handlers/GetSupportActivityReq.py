import betterproto
from game_server.net.session import Session
from lib.proto import GetSupportActivityReq,GetSupportActivityRsp

async def handle(session: Session, msg: GetSupportActivityReq) -> betterproto.Message:
    return GetSupportActivityRsp(retcode=0)
