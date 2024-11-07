import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetStageDropDisplayReq,
    GetStageDropDisplayRsp,
    StageDropDisplayInfo
)

async def handle(session: Session, msg: GetStageDropDisplayReq) -> betterproto.Message:
    return GetStageDropDisplayRsp(
        retcode=0,
        stage_drop_list=[
            StageDropDisplayInfo(
                stage_id=id
            )
            for id in msg.stage_id_list
        ]
    )
