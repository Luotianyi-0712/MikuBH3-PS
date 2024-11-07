import betterproto
from game_server.net.session import Session
from lib.proto import (
    ChapterBwWorldGetDataReq,
    ChapterBwWorldGetDataRsp,
    ChapterBwWorld,
    ChapterBwWorldRune,
    ChapterBwWorldTowerStage
)

async def handle(session: Session, msg: ChapterBwWorldGetDataReq) -> betterproto.Message:
    return ChapterBwWorldGetDataRsp(
        retcode=0,
        chapter_bw_world=ChapterBwWorld(
            chapter_id=msg.chapter_id
        )
    )
