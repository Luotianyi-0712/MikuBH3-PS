import betterproto
from game_server.net.session import Session
from lib.proto import GetOpenworldQuestActivityReq, GetOpenworldQuestActivityRsp

async def handle(session: Session, msg: GetOpenworldQuestActivityReq) -> betterproto.Message:
    return GetOpenworldQuestActivityRsp(retcode=0)
