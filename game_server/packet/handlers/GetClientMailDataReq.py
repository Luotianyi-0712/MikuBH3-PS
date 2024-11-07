import betterproto
from game_server.net.session import Session
from lib.proto import GetClientMailDataReq, GetClientMailDataRsp

async def handle(session: Session, msg: GetClientMailDataReq) -> betterproto.Message:
    return GetClientMailDataRsp(retcode=0)
