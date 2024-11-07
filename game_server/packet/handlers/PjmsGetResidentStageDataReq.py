
import betterproto
from game_server.net.session import Session
from lib.proto import (
    PjmsGetResidentStageDataReq,
    PjmsGetResidentStageDataRsp
)

async def handle(session: Session, msg: PjmsGetResidentStageDataReq) -> betterproto.Message:
    return PjmsGetResidentStageDataRsp(retcode=0)
