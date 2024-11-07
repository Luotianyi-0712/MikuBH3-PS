import betterproto
from game_server.net.session import Session
from lib.proto import StageBeginReq,StageBeginRsp

async def handle(session: Session, msg: StageBeginReq) -> betterproto.Message:
    return StageBeginRsp(
        retcode=0,
        stage_id=msg.stage_id,
        progress=0,
        is_collect_cheat_data=False
    )
