import betterproto
from game_server.net.session import Session
from utils.time import get_unix_in_seconds
from lib.proto import (
    GetWeekDayActivityDataReq,
    GetWeekDayActivityDataRsp,
    WeekDayActivity,
)


async def handle(
    session: Session, msg: GetWeekDayActivityDataReq
) -> betterproto.Message:
    return GetWeekDayActivityDataRsp(
        retcode=0,
        activity_list=[
            WeekDayActivity(
                activity_id=1003,
                stage_id_list=[101302, 101303, 101304, 101305],
                enter_times=1,
                begin_time=0,
                end_time=get_unix_in_seconds() + 3600 * 24 * 7,
                activity_begin_time=int(get_unix_in_seconds() * (10 / 8)),
                force_open_time=0,
            )
        ],
    )
