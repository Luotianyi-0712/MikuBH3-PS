import betterproto
from game_server.net.session import Session
from lib.proto import GetTrialAvatarReq,GetTrialAvatarRsp

async def handle(session: Session, msg: GetTrialAvatarReq) -> betterproto.Message:
    return GetTrialAvatarRsp(
        retcode=0,
        is_all_update=True
    )
