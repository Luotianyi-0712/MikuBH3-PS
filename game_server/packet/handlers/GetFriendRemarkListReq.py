import betterproto
from game_server.net.session import Session
from lib.proto import GetFriendRemarkListReq, GetFriendRemarkListRsp

async def handle(session: Session, msg: GetFriendRemarkListReq) -> betterproto.Message:
    return GetFriendRemarkListRsp(retcode=0)
