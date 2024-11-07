import betterproto
from game_server.net.session import Session
from lib.proto import GetGobackReq,GetGobackRsp

async def handle(session: Session, msg: GetGobackReq) -> betterproto.Message:
    return GetGobackRsp(retcode=0)
