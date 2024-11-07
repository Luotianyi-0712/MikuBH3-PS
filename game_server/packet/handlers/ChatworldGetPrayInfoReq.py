import betterproto
from game_server.net.session import Session
from lib.proto import ChatworldGetPrayInfoReq, ChatworldGetPrayInfoRsp

async def handle(session: Session, msg: ChatworldGetPrayInfoReq) -> betterproto.Message:
    return ChatworldGetPrayInfoRsp(retcode=0)
