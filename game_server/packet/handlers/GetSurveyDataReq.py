import betterproto
from game_server.net.session import Session
from lib.proto import GetSurveyDataReq, GetSurveyDataRsp

async def handle(session: Session, msg: GetSurveyDataReq) -> betterproto.Message:
    return GetSurveyDataRsp(retcode=0)
