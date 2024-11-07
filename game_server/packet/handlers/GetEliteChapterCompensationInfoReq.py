import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetEliteChapterCompensationInfoReq,
    GetEliteChapterCompensationInfoRsp,
    EliteChapterCompensationInfo
    
)

async def handle(session: Session, msg: GetEliteChapterCompensationInfoReq) -> betterproto.Message:
    return GetEliteChapterCompensationInfoRsp(
        retcode=0,
        chapter_list=[
            EliteChapterCompensationInfo(
                chapter_id=id,
                has_taken_compensation=True
            )
            for id in range(1,35)
        ]
    )
