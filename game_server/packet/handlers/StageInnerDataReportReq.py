import betterproto
from game_server.net.session import Session
from lib.proto import StageInnerDataReportReq,StageInnerDataReportRsp

async def handle(session: Session, msg: StageInnerDataReportReq) -> betterproto.Message:
    return StageInnerDataReportRsp(retcode=0)
