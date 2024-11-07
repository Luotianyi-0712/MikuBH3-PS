import betterproto
from game_server.net.session import Session
from lib.proto import PjmsGetStoryDataReq,PjmsGetStoryDataRsp

async def handle(session: Session, msg: PjmsGetStoryDataReq) -> betterproto.Message:
    return PjmsGetStoryDataRsp(retcode=0)
