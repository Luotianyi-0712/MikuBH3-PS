import betterproto
from game_server.net.session import Session
from lib.proto import GetProductRecommendListReq, GetProductRecommendListRsp

async def handle(session: Session, msg: GetProductRecommendListReq) -> betterproto.Message:
    return GetProductRecommendListRsp(
        retcode=0,
        recommend_list=[16301720]
    )
