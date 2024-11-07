import betterproto
from game_server.net.session import Session
from lib.proto import GetChatgroupListReq, GetChatgroupListRsp

async def handle(session: Session, msg: GetChatgroupListReq) -> betterproto.Message:
    return GetChatgroupListRsp(retcode=0)
