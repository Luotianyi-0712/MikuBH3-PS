import betterproto
from game_server.net.session import Session
from lib.proto import (
    LoginWishGetMainDataReq,
    LoginWishGetMainDataRsp,
    LoginWishActivity
)

async def handle(session: Session, msg: LoginWishGetMainDataReq) -> betterproto.Message:
    return LoginWishGetMainDataRsp(
        retcode=0,
        activity_list=[
            LoginWishActivity(
                activity_id=19,
                begin_time=1729540800,
                end_time=1880308800,
                login_days=1,
                show_begin_time=1729454400,
                show_end_time=1880308800
            )
        ]
    )
