import betterproto
from game_server.net.session import Session
from lib.proto import GetTowerRaidActivityReq,GetTowerRaidActivityRsp

async def handle(session: Session, msg: GetTowerRaidActivityReq) -> betterproto.Message:
    return GetTowerRaidActivityRsp(retcode=0)
