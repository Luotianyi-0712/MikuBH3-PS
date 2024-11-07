import betterproto
from game_server.net.session import Session
from game_server.utils import get_unix_in_seconds
from lib.proto import (
    GetLoginActivityReq,
    GetLoginActivityRsp,
    LoginActivityData
)

async def handle(session: Session, msg: GetLoginActivityReq) -> betterproto.Message:
    return GetLoginActivityRsp(
        retcode=0,
        login_list=[
            LoginActivityData(
                id=581,
                login_days=get_unix_in_seconds(),
                accept_time=get_unix_in_seconds(),
                duration_end_time=get_unix_in_seconds() + 604800 * 2
            )
        ]
    )
