import betterproto
from game_server.net.session import Session
from lib.proto import (
    ChapterArkGetDataReq,
    ChapterArkGetDataRsp,
    ChapterArk,
    ChapterArkRoleInfo,
    ChapterArkSkillInfo,
    ChapterArkSupSkillInfo
    
)

async def handle(session: Session, msg: ChapterArkGetDataReq) -> betterproto.Message:
    avatar_lists = [1,2,3,4,5]
    return ChapterArkGetDataRsp(
        retcode=0,
        chapter_ark=ChapterArk(
            chapter_id=msg.chapter_id,
            avatar_list=avatar_lists,
            is_finish_opening=True,
            role_list=[
                ChapterArkRoleInfo(
                    id=id,
                    level=30
                )
                for id in avatar_lists
            ],
            skill_list=[
                ChapterArkSkillInfo(
                    id=i * 100 + j,
                    level=3 if j > 3 else 1
                )
                for i in range(1, 6)
                for j in range(1, 13)
            ]
        )
    )
