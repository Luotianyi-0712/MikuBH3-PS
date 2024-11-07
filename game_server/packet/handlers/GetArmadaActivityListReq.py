import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetArmadaActivityListReq,
    GetArmadaActivityListRsp,
    ArmadaActivity,
    ArmadaActivityType
)

async def handle(session: Session, msg: GetArmadaActivityListReq) -> betterproto.Message:
    return GetArmadaActivityListRsp(
        retcode=0,
        activity_list=[
            ArmadaActivity(
                begin_time=0,
                end_time=1880308800,
                type=ArmadaActivityType.ARMADA_ACTIVITY_ARMADA_STAGE_SCORE_ACTIVITY.value
            )
        ]
    )
