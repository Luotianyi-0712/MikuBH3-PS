import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetInviteActivityInviteeDataReq,
    GetInviteActivityInviteeDataRsp,
    InviteeActivity,
    InviteeActivityType
)

async def handle(session: Session, msg: GetInviteActivityInviteeDataReq) -> betterproto.Message:
    return GetInviteActivityInviteeDataRsp(
        retcode=0,
        invitee_activity_info_list=[
            InviteeActivity(
                schedule_id=2,
                activity_type=InviteeActivityType.INVITEE_ACTIVITY_TYPE_GOBACK
            )
        ]
    )
