import betterproto
from game_server.net.session import Session
from lib.proto import GetConsignedOrderDataReq, GetConsignedOrderDataRsp

async def handle(session: Session, msg: GetConsignedOrderDataReq) -> betterproto.Message:
    return GetConsignedOrderDataRsp(retcode=0)
