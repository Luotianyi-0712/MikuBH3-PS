import betterproto
from game_server.net.session import Session
from lib.proto import GetMasterPupilCardReq, GetMasterPupilCardRsp

async def handle(session: Session, msg: GetMasterPupilCardReq) -> betterproto.Message:
    return GetMasterPupilCardRsp(retcode=0)
