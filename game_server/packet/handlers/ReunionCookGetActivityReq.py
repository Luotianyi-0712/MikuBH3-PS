import betterproto
from game_server.net.session import Session
from lib.proto import ReunionCookGetActivityReq,ReunionCookGetActivityRsp

async def handle(session: Session, msg: ReunionCookGetActivityReq) -> betterproto.Message:
    return ReunionCookGetActivityRsp(retcode=0)
