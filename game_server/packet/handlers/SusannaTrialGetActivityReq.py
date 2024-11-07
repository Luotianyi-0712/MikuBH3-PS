import betterproto
from game_server.net.session import Session
from lib.proto import SusannaTrialGetActivityReq,SusannaTrialGetActivityRsp

async def handle(session: Session, msg: SusannaTrialGetActivityReq) -> betterproto.Message:
    return SusannaTrialGetActivityRsp(retcode=0)
