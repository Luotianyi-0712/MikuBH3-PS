import betterproto
from game_server.net.session import Session
from lib.proto import GetNewOpenworldReq, GetNewOpenworldRsp

async def handle(session: Session, msg: GetNewOpenworldReq) -> betterproto.Message:
    return GetNewOpenworldRsp(retcode=0)
