import betterproto
from game_server.net.session import Session
from lib.proto import GetExBossScheduleReq, GetExBossScheduleRsp

async def handle(session: Session, msg: GetExBossScheduleReq) -> betterproto.Message:
    return GetExBossScheduleRsp(
        retcode=0,
        begin_time=1730750400,
        end_time=1931268799,
        min_level=38,
        rank_id=104,
        schedule_id=10377
    )
