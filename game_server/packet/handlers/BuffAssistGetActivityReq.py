import betterproto
from game_server.net.session import Session
from lib.proto import BuffAssistGetActivityReq,BuffAssistGetActivityRsp

async def handle(session: Session, msg: BuffAssistGetActivityReq) -> betterproto.Message:
    return BuffAssistGetActivityRsp(retcode=0)
