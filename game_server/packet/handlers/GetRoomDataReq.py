import betterproto
from game_server.net.session import Session
from lib.proto import GetRoomDataReq,GetRoomDataRsp

async def handle(session: Session, msg: GetRoomDataReq) -> betterproto.Message:
    return GetRoomDataRsp(retcode=0)
