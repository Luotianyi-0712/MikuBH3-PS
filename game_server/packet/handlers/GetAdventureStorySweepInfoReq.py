import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetAdventureStorySweepInfoReq,
    GetAdventureStorySweepInfoRsp,
    IslandStorySweepData
)

async def handle(session: Session, msg: GetAdventureStorySweepInfoReq) -> betterproto.Message:
    return GetAdventureStorySweepInfoRsp(
        retcode=0,
        story_sweep_list=[
            IslandStorySweepData(
                avatar_id_list=[
                    20401,
                    20301,
                    20201
                ],
                is_finished=True,
                over_time=1719938652,
                sweep_id=282
            ),
            IslandStorySweepData(
                avatar_id_list=[
                    3701,
                    3601,
                    3501
                ],
                is_finished=True,
                over_time=1719938654,
                sweep_id=282
            ),
            IslandStorySweepData(
                avatar_id_list=[
                    3301,
                    3201,
                    3101
                ],
                is_finished=True,
                over_time=1719938655,
                sweep_id=282
            ),
        ]
    )
