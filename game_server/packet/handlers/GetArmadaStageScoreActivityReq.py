import betterproto
from game_server.net.session import Session
from lib.proto import GetArmadaStageScoreActivityReq, GetArmadaStageScoreActivityRsp

async def handle(session: Session, msg: GetArmadaStageScoreActivityReq) -> betterproto.Message:
    return GetArmadaStageScoreActivityRsp(retcode=0)
