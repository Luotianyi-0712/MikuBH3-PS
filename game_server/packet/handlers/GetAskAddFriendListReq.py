import betterproto
from game_server.net.session import Session
from lib.proto import GetAskAddFriendListReq, GetAskAddFriendListRsp

async def handle(session: Session, msg: GetAskAddFriendListReq) -> betterproto.Message:
    return GetAskAddFriendListRsp(retcode=0)
