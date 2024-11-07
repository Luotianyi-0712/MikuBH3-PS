import betterproto
from game_server.net.session import Session
from lib.proto import GetFarmActivityDataReq, GetFarmActivityDataRsp

async def handle(session: Session, msg: GetFarmActivityDataReq) -> betterproto.Message:
    return GetFarmActivityDataRsp(retcode=0)
