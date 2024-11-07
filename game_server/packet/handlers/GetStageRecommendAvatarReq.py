import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetStageRecommendAvatarReq,
    GetStageRecommendAvatarRsp,
    StageRecommendAvatar
)

async def handle(session: Session, msg: GetStageRecommendAvatarReq) -> betterproto.Message:
    return GetStageRecommendAvatarRsp(
        retcode=0,
        stage_recommend_avatar_list=[
            StageRecommendAvatar(
                id=f"{id}",
                type=msg.type
            )
            for id in msg.id_list
        ]
    )
