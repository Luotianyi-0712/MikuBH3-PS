import betterproto
from game_server.net.session import Session
from lib.proto import GetExBossScheduleReq, GetExBossScheduleRsp

async def handle(session: Session, msg: GetExBossScheduleReq) -> betterproto.Message:
    return GetExBossScheduleRsp(retcode=0)
