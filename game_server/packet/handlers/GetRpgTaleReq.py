import betterproto
from game_server.net.session import Session
from lib.proto import GetRpgTaleReq,GetRpgTaleRsp

async def handle(session: Session, msg: GetRpgTaleReq) -> betterproto.Message:
    return GetRpgTaleRsp(retcode=0)
