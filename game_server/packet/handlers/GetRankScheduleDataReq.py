import betterproto
from game_server.net.session import Session
from lib.proto import GetRankScheduleDataReq,GetRankScheduleDataRsp

async def handle(session: Session, msg: GetRankScheduleDataReq) -> betterproto.Message:
    return GetRankScheduleDataRsp(retcode=0)
