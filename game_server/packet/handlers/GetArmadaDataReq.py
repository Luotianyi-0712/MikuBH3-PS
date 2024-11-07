import betterproto
from game_server.net.session import Session
from lib.proto import GetArmadaDataReq, GetArmadaDataRsp

async def handle(session: Session, msg: GetArmadaDataReq) -> betterproto.Message:
    return GetArmadaDataRsp(retcode=0)
