import betterproto
from game_server.net.session import Session
from lib.proto import GetMosaicActivityReq, GetMosaicActivityRsp

async def handle(session: Session, msg: GetMosaicActivityReq) -> betterproto.Message:
    return GetMosaicActivityRsp(retcode=0)
