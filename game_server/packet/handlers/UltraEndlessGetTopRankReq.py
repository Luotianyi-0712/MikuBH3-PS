import betterproto
import random
from game_server.net.session import Session
from lib.proto import (
    UltraEndlessGetTopRankReq,
    UltraEndlessGetTopRankRsp,
    RankShowData,
    UserRankData
)

async def handle(session: Session, msg: UltraEndlessGetTopRankReq) -> betterproto.Message:
    return UltraEndlessGetTopRankRsp(
        retcode=0,
        schedule_id=3363,
        rank_data=RankShowData(
            rank_list=[
                UserRankData(
                    avatar_id=205,
                    custom_head_id=161100,
                    frame_id=200001,
                    nick_name="Miku",
                    rank=1,
                    score=5021766,
                    uid=1337,
                    ultra_endless_group_level=9
                )
            ]
        )
    )
