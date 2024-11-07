import betterproto
from game_server.net.session import Session
from lib.proto import GetFriendListReq, GetFriendListRsp

async def handle(session: Session, msg: GetFriendListReq) -> betterproto.Message:
    return GetFriendListRsp(retcode=0)
