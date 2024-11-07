import betterproto
from game_server.net.session import Session
from lib.proto import GetWarshipTrialDataReq, GetWarshipTrialDataRsp

async def handle(session: Session, msg: GetWarshipTrialDataReq) -> betterproto.Message:
    return GetWarshipTrialDataRsp(retcode=0,is_all=True)
