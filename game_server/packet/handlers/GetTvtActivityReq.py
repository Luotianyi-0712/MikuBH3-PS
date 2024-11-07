import betterproto
from game_server.net.session import Session
from lib.proto import GetTvtActivityReq,GetTvtActivityRsp

async def handle(session: Session, msg: GetTvtActivityReq) -> betterproto.Message:
    return GetTvtActivityRsp(retcode=0)
