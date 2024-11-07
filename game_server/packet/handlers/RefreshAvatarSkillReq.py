import betterproto
from game_server.net.session import Session
from lib.proto import (
    RefreshAvatarSkillReq,
    RefreshAvatarSkillRsp
)

async def handle(session: Session, msg: RefreshAvatarSkillReq) -> betterproto.Message:
    return RefreshAvatarSkillRsp(retcode=0)
