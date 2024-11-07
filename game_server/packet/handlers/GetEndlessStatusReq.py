import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetEndlessStatusReq,
    GetEndlessStatusRsp,
    EndlessStatus,
    EndlessType
)

async def handle(session: Session, msg: GetEndlessStatusReq) -> betterproto.Message:
    return GetEndlessStatusRsp(
        retcode=0,
        cur_status=EndlessStatus(
            begin_time=1730098800,
            can_join_in=True,
            close_time=1880308800,
            end_time=1880308800,
            endless_type=EndlessType.ENDLESS_TYPE_ULTRA.value,
        ),
        next_status_list=[
            EndlessStatus(
                begin_time=1730444400,
                close_time=1880308800,
                end_time=1880308800,
                endless_type=EndlessType.ENDLESS_TYPE_ULTRA.value
            )
        ],
        selected_endless_type=5
    )
