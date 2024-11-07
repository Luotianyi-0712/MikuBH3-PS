import betterproto
from game_server.net.session import Session
from lib.proto import GetRecommendGoodsReq, GetRecommendGoodsRsp

async def handle(session: Session, msg: GetRecommendGoodsReq) -> betterproto.Message:
    return GetRecommendGoodsRsp(retcode=0)
