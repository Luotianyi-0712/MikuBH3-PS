import betterproto
from game_server.net.session import Session
from lib.proto import GetCardProductInfoReq,GetCardProductInfoRsp

async def handle(session: Session, msg: GetCardProductInfoReq) -> betterproto.Message:
    return GetCardProductInfoRsp(retcode=0)
