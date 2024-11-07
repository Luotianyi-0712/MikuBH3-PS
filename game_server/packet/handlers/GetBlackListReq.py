import betterproto
from game_server.net.session import Session
from lib.proto import GetBlackListReq, GetBlackListRsp

async def handle(session: Session, msg: GetBlackListReq) -> betterproto.Message:
    return GetBlackListRsp(retcode=0)
