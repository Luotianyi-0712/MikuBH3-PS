import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetThemeWantedReq,
    GetThemeWantedRsp,
    ThemeWantedActivity,
    ThemeWantedStageGroupInfo
)

async def handle(session: Session, msg: GetThemeWantedReq) -> betterproto.Message:
    return GetThemeWantedRsp(
        retcode=0,
        theme_wanted_activity=ThemeWantedActivity(
            activity_id=11105,
            open_stage_group_id_list=[17,18,19,20],
            schedule_id=5,
            stage_group_info_list=[
                ThemeWantedStageGroupInfo(
                    progress=8,
                    stage_group_id=17
                ),
                ThemeWantedStageGroupInfo(
                    not_pass_progress_list=[7],
                    progress=7,
                    stage_group_id=18
                ),
                ThemeWantedStageGroupInfo(
                    progress=8,
                    stage_group_id=19
                ),
                ThemeWantedStageGroupInfo(
                    progress=8,
                    stage_group_id=20
                )
            ]
        )
    )
