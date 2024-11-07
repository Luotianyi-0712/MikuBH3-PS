import betterproto
from game_server.net.session import Session
from lib.proto import GetWeeklyRoutineActivityReq,GetWeeklyRoutineActivityRsp

async def handle(session: Session, msg: GetWeeklyRoutineActivityReq) -> betterproto.Message:
    return GetWeeklyRoutineActivityRsp(retcode=0)
