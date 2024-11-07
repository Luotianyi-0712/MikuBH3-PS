
import betterproto
from game_server.net.session import Session
from lib.proto import GetOfflineResourceDataReq,GetOfflineResourceDataRsp

async def handle(session: Session, msg: GetOfflineResourceDataReq) -> betterproto.Message:
    return GetOfflineResourceDataRsp(retcode=0)
