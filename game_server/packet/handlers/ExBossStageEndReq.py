import betterproto
from game_server.net.session import Session
from lib.proto import (
    ExBossStageEndReq,
    ExBossStageEndRsp
)

async def handle(session: Session, msg: ExBossStageEndReq) -> betterproto.Message:
    return ExBossStageEndRsp(
        retcode=0,
        boss_id=msg.boss_id,
        end_status=msg.end_status
    )
