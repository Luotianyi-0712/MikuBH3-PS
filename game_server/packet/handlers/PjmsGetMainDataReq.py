
import betterproto
from game_server.net.session import Session
from lib.proto import (
    PjmsGetMainDataReq,
    PjmsGetMainDataRsp
)

async def handle(session: Session, msg: PjmsGetMainDataReq) -> betterproto.Message:
    return PjmsGetMainDataRsp(retcode=0)
