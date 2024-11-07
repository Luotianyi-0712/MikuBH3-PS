import betterproto
from game_server.net.session import Session
from lib.proto import GetGardenScheduleReq, GetGardenScheduleRsp

async def handle(session: Session, msg: GetGardenScheduleReq) -> betterproto.Message:
    return GetGardenScheduleRsp(retcode=0)
