import betterproto
from game_server.net.session import Session
from lib.proto import GetAssistantFrozenListReq, GetAssistantFrozenListRsp

async def handle(session: Session, msg: GetAssistantFrozenListReq) -> betterproto.Message:
    return GetAssistantFrozenListRsp(retcode=0)
