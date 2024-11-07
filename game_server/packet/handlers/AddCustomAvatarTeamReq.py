
import betterproto
from game_server.net.session import Session
from lib.proto import (
    AddCustomAvatarTeamReq,
    AddCustomAvatarTeamRsp
)

async def handle(session: Session, msg: AddCustomAvatarTeamReq) -> betterproto.Message:
    return AddCustomAvatarTeamRsp(retcode=0)
