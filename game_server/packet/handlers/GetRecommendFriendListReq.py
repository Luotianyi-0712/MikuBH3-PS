import betterproto
from game_server.net.session import Session
from lib.proto import GetRecommendFriendListReq, GetRecommendFriendListRsp

async def handle(session: Session, msg: GetRecommendFriendListReq) -> betterproto.Message:
    return GetRecommendFriendListRsp(retcode=0)
