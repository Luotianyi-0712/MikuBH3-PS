import betterproto
from game_server.net.session import Session
from lib.proto import GetSecurityPasswordReq, GetSecurityPasswordRsp

async def handle(session: Session, msg: GetSecurityPasswordReq) -> betterproto.Message:
    return GetSecurityPasswordRsp(retcode=0)
