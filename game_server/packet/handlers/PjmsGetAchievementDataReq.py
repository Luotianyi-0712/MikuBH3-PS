import betterproto
from game_server.net.session import Session
from lib.proto import PjmsGetAchievementDataReq,PjmsGetAchievementDataRsp

async def handle(session: Session, msg: PjmsGetAchievementDataReq) -> betterproto.Message:
    return PjmsGetAchievementDataRsp(retcode=0)
