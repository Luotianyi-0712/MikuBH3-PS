import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetInviteActivityInviterDataReq,
    GetInviteActivityInviterDataRsp,
    InviterActivity
)

async def handle(session: Session, msg: GetInviteActivityInviterDataReq) -> betterproto.Message:
    return GetInviteActivityInviterDataRsp(
        retcode=0,
        inviter_activity_info_list=[
            InviterActivity(
                schedule_id=4
            ),
            InviterActivity(
                schedule_id=103
            ),
        ],
        my_invite_code="17263334YG"
    )
