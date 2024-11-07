import betterproto
from game_server.net.session import Session
from lib.proto import GetDLCTowerReq, GetDLCTowerRsp

async def handle(session: Session, msg: GetDLCTowerReq) -> betterproto.Message:
    return GetDLCTowerRsp(retcode=0,schedule_id=203)
