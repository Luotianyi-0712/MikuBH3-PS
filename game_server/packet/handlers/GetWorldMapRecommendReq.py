import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetWorldMapRecommendReq,
    GetWorldMapRecommendRsp,
    WorldMapRecommend
)


async def handle(session: Session, msg: GetWorldMapRecommendReq) -> betterproto.Message:
    return GetWorldMapRecommendRsp(
        retcode=0,
        activity_recommend_list=[
            WorldMapRecommend(
                weight=110,
                world_map_id=2317
            ),
            WorldMapRecommend(
                weight=100,
                world_map_id=2321
            )
        ],
        permanent_recommend_list=[
            WorldMapRecommend(
                active_condition_list=[
                    201
                ],
                weight=2,
                world_map_id=9
            ),
            WorldMapRecommend(
                weight=100,
                world_map_id=7
            ),
            WorldMapRecommend(
                active_condition_list=[
                    207
                ],
                weight=-100,
                world_map_id=7
            ),
            WorldMapRecommend(
                weight=86,
                world_map_id=8
            ),
            WorldMapRecommend(
                active_condition_list=[
                    214,
                    215
                ],
                weight=1,
                world_map_id=11
            ),
            WorldMapRecommend(
                active_condition_list=[
                    216
                ],
                weight=45,
                world_map_id=18
            ),
            WorldMapRecommend(
                weight=60,
                world_map_id=1
            ),
            WorldMapRecommend(
                weight=50,
                world_map_id=2107
            ),
            WorldMapRecommend(
                weight=70,
                world_map_id=1004
            )
        ]
    )


