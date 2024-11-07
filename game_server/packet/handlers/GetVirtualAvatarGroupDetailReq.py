import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetVirtualAvatarGroupDetailReq,
    GetVirtualAvatarGroupDetailRsp,
    VirtualAvatarGroup,
    VirtualAvatar
)

async def handle(session: Session, msg: GetVirtualAvatarGroupDetailReq) -> betterproto.Message:
    rsp = GetVirtualAvatarGroupDetailRsp(retcode=0)
    if msg.group_id == 114:
        rsp.virtual_avatar_group = VirtualAvatarGroup(
            group_id=114,
            virtual_avatar_list=[
                VirtualAvatar(
                    virtual_avatar_id=300001
                ),
                VirtualAvatar(
                    virtual_avatar_id=300003
                ),
            ],
            virtual_avatar_team_list=[300001,300003]
        )
    if msg.group_id == 111:
        rsp.virtual_avatar_group = VirtualAvatarGroup(
            group_id=114,
            virtual_avatar_list=[
                VirtualAvatar(
                    virtual_avatar_id=300001
                )
            ],
            virtual_avatar_team_list=[300001]
        )
    return rsp