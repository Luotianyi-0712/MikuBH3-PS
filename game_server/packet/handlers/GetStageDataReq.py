import betterproto
from game_server.net.session import Session
from game_server.resource import ResourceManager
from game_server.resource.configdb.stage_data_main import StageDataMain
from lib.proto import (
    GetStageDataReq,
    GetStageDataRsp,
    Stage,
    StageEventData
)

async def handle(session: Session, msg: GetStageDataReq) -> betterproto.Message:
    stage_list : Stage = [
        Stage(
            id=stage.levelId,
            progress=1,
            challenge_index_list=[0,1,2] if len(stage.challengeList) == 3 else [0],
            is_done=True,
            max_rank=1
        )
        for stage in ResourceManager.instance().values(StageDataMain)
    ]
    
    return GetStageDataRsp(
        retcode=0,
        is_all=True,
        stage_list=stage_list,
        finished_chapter_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,36,43],
        event_data_list=[
            StageEventData(
                begin_time=1729108800,
                end_time=1990911600,
                chapter_id=200,
                unlock_level=30
            )
        ]
    )
