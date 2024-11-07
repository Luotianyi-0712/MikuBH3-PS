import betterproto
from game_server.net.session import Session
from lib.proto import GetMasterPupilMainDataReq, GetMasterPupilMainDataRsp

async def handle(session: Session, msg: GetMasterPupilMainDataReq) -> betterproto.Message:
    return GetMasterPupilMainDataRsp(retcode=0)
