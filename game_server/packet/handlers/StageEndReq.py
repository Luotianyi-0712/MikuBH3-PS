import betterproto
from game_server.net.session import Session
from lib.proto import (
    StageEndReq,
    StageEndRsp,
    StageEndReqBody
)

async def handle(session: Session, msg: StageEndReq) -> betterproto.Message:
    ms = memoryview(b"".join(msg.body))
    req = StageEndReqBody()
    req.parse(ms.tobytes())
    return StageEndRsp(
        retcode=0,
        stage_id=req.stage_id,
        end_status=req.end_status
    )
