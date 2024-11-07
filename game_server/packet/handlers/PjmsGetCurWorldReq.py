import betterproto
from game_server.net.session import Session
from lib.proto import (PjmsGetCurWorldReq,PjmsGetCurWorldRsp)

async def handle(session: Session, msg: PjmsGetCurWorldReq) -> betterproto.Message:
    return PjmsGetCurWorldRsp(retcode=0)
