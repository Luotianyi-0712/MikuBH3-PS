import betterproto
from game_server.net.session import Session
from lib.proto import GetMasterPupilDataReq, GetMasterPupilDataRsp

async def handle(session: Session, msg: GetMasterPupilDataReq) -> betterproto.Message:
    return GetMasterPupilDataRsp(retcode=0)
