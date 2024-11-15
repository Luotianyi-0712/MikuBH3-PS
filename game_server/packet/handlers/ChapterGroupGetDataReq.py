import betterproto
from game_server.net.session import Session
from lib.proto import (
    ChapterGroupGetDataReq,
    ChapterGroupGetDataRsp,
    ChapterGroup,
    ChapterGroupSite,
    ChapterGroupSiteStatus
)

async def handle(session: Session, msg: ChapterGroupGetDataReq) -> betterproto.Message:
    rsp = ChapterGroupGetDataRsp(
        retcode=0,
        is_all=True,
        chapter_group_list=[
            ChapterGroup(
                id=1,
                site_list=[
                    ChapterGroupSite(
                        chapter_id=1,
                        site_id=1,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=2,
                        site_id=2,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    )
                ]
            ),
            ChapterGroup(
                id=2,
                site_list=[
                    ChapterGroupSite(
                        chapter_id=3,
                        site_id=3,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=4,
                        site_id=4,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=5,
                        site_id=5,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=6,
                        site_id=6,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    )
                ]
            ),
            ChapterGroup(
                id=3,
                site_list=[
                    ChapterGroupSite(
                        chapter_id=7,
                        site_id=7,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=8,
                        site_id=8,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=9,
                        site_id=9,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=10,
                        site_id=10,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=11,
                        site_id=11,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    )
                ]
            ),
            ChapterGroup(
                id=4,
                site_list=[
                    ChapterGroupSite(
                        chapter_id=12,
                        site_id=12,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=13,
                        site_id=13,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=14,
                        site_id=14,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=15,
                        site_id=15,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    )
                ]
            ),
            ChapterGroup(
                id=5,
                site_list=[
                    ChapterGroupSite(
                        chapter_id=16,
                        site_id=16,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=17,
                        site_id=17,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    )
                ]
            ),
            ChapterGroup(
                id=6,
                site_list=[
                    ChapterGroupSite(
                        chapter_id=18,
                        site_id=18,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=19,
                        site_id=19,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=20,
                        site_id=20,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    )
                ]
            ),
            ChapterGroup(
                id=7,
                site_list=[
                    ChapterGroupSite(
                        chapter_id=21,
                        site_id=21,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=22,
                        site_id=22,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    )
                ]
            ),
            ChapterGroup(
                id=8,
                site_list=[
                    ChapterGroupSite(
                        chapter_id=23,
                        site_id=23,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=24,
                        site_id=24,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=25,
                        site_id=25,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    )
                ]
            ),
            ChapterGroup(
                id=9,
                site_list=[
                    ChapterGroupSite(
                        chapter_id=26,
                        site_id=26,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=27,
                        site_id=27,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=28,
                        site_id=28,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    )
                ]
            ),
            ChapterGroup(
                id=10,
                site_list=[
                    ChapterGroupSite(
                        chapter_id=29,
                        site_id=29,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=30,
                        site_id=30,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    )
                ]
            ),
            ChapterGroup(
                id=11,
                site_list=[
                    ChapterGroupSite(
                        chapter_id=31,
                        site_id=31,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    )
                ]
            ),
            ChapterGroup(
                id=12,
                site_list=[
                    ChapterGroupSite(
                        chapter_id=32,
                        site_id=32,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=33,
                        site_id=33,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=34,
                        site_id=34,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_LOCKED.value
                    )
                ]
            ),
            ChapterGroup(
                id=13,
                site_list=[
                    ChapterGroupSite(
                        chapter_id=36,
                        site_id=36,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    ),
                    ChapterGroupSite(
                        chapter_id=37,
                        site_id=37,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    )
                ]
            ),
            ChapterGroup(
                id=14,
                site_list=[
                    ChapterGroupSite(
                        chapter_id=40,
                        site_id=40,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    )
                ]
            ),
            ChapterGroup(
                id=15,
                site_list=[
                    ChapterGroupSite(
                        chapter_id=43,
                        site_id=43,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    )
                ]
            ),
            ChapterGroup(
                id=16,
                site_list=[
                    ChapterGroupSite(
                        chapter_id=100,
                        site_id=100,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    )
                ]
            ),
            ChapterGroup(
                id=17,
                site_list=[
                    ChapterGroupSite(
                        chapter_id=150,
                        site_id=150,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    )
                ]
            ),
            ChapterGroup(
                id=18,
                site_list=[
                    ChapterGroupSite(
                        chapter_id=200,
                        site_id=200,
                        status=ChapterGroupSiteStatus.CHAPTER_GROUP_SITE_STATUS_FINISHED.value
                    )
                ]
            )
        ]
    )

    return rsp
