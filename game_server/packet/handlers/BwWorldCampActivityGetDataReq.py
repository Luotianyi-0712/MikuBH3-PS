import betterproto
from game_server.net.session import Session
from lib.proto import BwWorldCampActivityGetDataReq, BwWorldCampActivityGetDataRsp

async def handle(session: Session, msg: BwWorldCampActivityGetDataReq) -> betterproto.Message:
    return BwWorldCampActivityGetDataRsp(retcode=0)
