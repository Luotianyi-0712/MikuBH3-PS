import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetExBossRankReq,
    GetExBossRankRsp,
    RankShowData,
    UserRankData
)

async def handle(session: Session, msg: GetExBossRankReq) -> betterproto.Message:
    return GetExBossRankRsp(
        retcode=0,
        rank_id=104,
        rank_data=RankShowData(
            my_rank=104,
            my_rank_type=2,
            my_score=116330,
            rank_list=[
                UserRankData(
                    avatar_id=3101,
                    custom_head_id=161099,
                    dress_id=50217,
                    frame_id=200080,
                    nick_name="Miku",
                    rank=1,
                    score=119727,
                    uid=1337
                )
            ]
        ),
        boss_id=51016
    )
