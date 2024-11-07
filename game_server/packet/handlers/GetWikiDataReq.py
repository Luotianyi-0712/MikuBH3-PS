import betterproto
from game_server.net.session import Session
from lib.proto import GetWikiDataReq, GetWikiDataRsp

async def handle(session: Session, msg: GetWikiDataReq) -> betterproto.Message:
    return GetWikiDataRsp(
        retcode=0,
        has_take_activity_suit_reward_list=[132],
        has_take_rating_reward_list=[1,2,3,4,5,6]
    )
