import betterproto
from game_server.net.session import Session
from lib.proto import ChatworldBeastGetActivityReq, ChatworldBeastGetActivityRsp

async def handle(session: Session, msg: ChatworldBeastGetActivityReq) -> betterproto.Message:
    return ChatworldBeastGetActivityRsp(retcode=0)
