import betterproto
from game_server.net.session import Session
from lib.proto import (
    PjmsGetActivityPanelReq,
    PjmsGetActivityPanelRsp,
    PjmsActivityPanel
)

async def handle(session: Session, msg: PjmsGetActivityPanelReq) -> betterproto.Message:
    return PjmsGetActivityPanelRsp(
        retcode=0,
        activity_panel_list=[
            PjmsActivityPanel(
                activity_id=1001,
                advance_begin_time=1712800800,
                advance_end_time=1716494399,
                begin_time=1712800800,
                end_time=4294967295,
                is_resident=True,
                min_level=30
            ),
            PjmsActivityPanel(
                activity_id=1002,
                advance_begin_time=1718848800,
                advance_end_time=1721851199,
                begin_time=1718848800,
                end_time=4294967295,
                is_resident=True,
                min_level=30
            ),
            PjmsActivityPanel(
                activity_id=1003,
                advance_begin_time=1718157600,
                advance_end_time=1725479999,
                begin_time=1712887200,
                end_time=4294967295,
                is_resident=True,
                min_level=30
            ),
            PjmsActivityPanel(
                activity_id=1004,
                advance_begin_time=1726452000,
                advance_end_time=1729108799,
                begin_time=1726452000,
                end_time=4294967295,
                is_resident=True,
                min_level=30
            )
        ]
    )
