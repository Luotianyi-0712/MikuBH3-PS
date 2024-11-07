import betterproto
from game_server.net.session import Session
from lib.proto import GetNinjaActivityReq,GetNinjaActivityRsp

async def handle(session: Session, msg: GetNinjaActivityReq) -> betterproto.Message:
    return GetNinjaActivityRsp(retcode=0)
