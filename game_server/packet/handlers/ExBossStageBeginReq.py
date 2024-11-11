import betterproto
from game_server.net.session import Session
from lib.proto import (
    ExBossStageBeginReq,
    ExBossStageBeginRsp
)

async def handle(session: Session, msg: ExBossStageBeginReq) -> betterproto.Message:
    return ExBossStageBeginRsp(
        retcode=0
    )
