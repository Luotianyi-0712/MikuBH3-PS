import betterproto
from game_server.net.session import Session
from lib.proto import PjmsGetConditionDataReq,PjmsGetConditionDataRsp

async def handle(session: Session, msg: PjmsGetConditionDataReq) -> betterproto.Message:
    return PjmsGetConditionDataRsp(retcode=0)
