import betterproto
from game_server.net.session import Session
from lib.proto import GetAvatarMissionActivityReq,GetAvatarMissionActivityRsp

async def handle(session: Session, msg: GetAvatarMissionActivityReq) -> betterproto.Message:
    return GetAvatarMissionActivityRsp(retcode=0)
