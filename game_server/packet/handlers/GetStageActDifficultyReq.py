import betterproto
from game_server.net.session import Session
from game_server.resource import ResourceManager
from game_server.resource.configdb.act_challenge_data import ActChallengeData
from lib.proto import (
    GetStageActDifficultyReq,
    GetStageActDifficultyRsp,
    StageActDifficultyInfo
)

async def handle(session: Session, msg: GetStageActDifficultyReq) -> betterproto.Message:
    return GetStageActDifficultyRsp(
        retcode=0,
        act_difficulty_list=[
            StageActDifficultyInfo(
                act_id=act.actId,
                difficulty=act.difficulty,
                has_take_challenge_num_index=[1,2,3]
            )
            for act in ResourceManager.instance().values(ActChallengeData)
        ]
    )
