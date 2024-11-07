import betterproto
from game_server.net.session import Session
from lib.proto import (
    GeneralActivityGetMainInfoReq,
    GeneralActivityGetMainInfoRsp,
    GeneralActivity,
    GeneralActivityBasicInfo
)

async def handle(session: Session, msg: GeneralActivityGetMainInfoReq) -> betterproto.Message:
    return GeneralActivityGetMainInfoRsp(
        retcode=0,
        activity_list=[
            GeneralActivity(
                general_basic_info=GeneralActivityBasicInfo(
                    activity_id=50000001,
                    schedule_id=412,
                    series_activity_id=[50000001]
                )
            )
        ]
    )
