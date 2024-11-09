import betterproto
from game_server.net.session import Session
from utils.time import get_unix_in_seconds
from game_server.resource import ResourceManager
from game_server.resource.configdb.general_activity_stage_group import GeneralActivityStageGroupData
from game_server.resource.configdb.general_activity import GeneralActivityData
from lib.proto import (
    GeneralActivityGetMainInfoReq,
    GeneralActivityGetMainInfoRsp,
    GeneralActivity,
    GeneralActivityBasicInfo,
    GeneralActivityStage,
    GeneralActivityStageGroupScheduleInfo
)

async def handle(session: Session, msg: GeneralActivityGetMainInfoReq) -> betterproto.Message:

    activity_list = []
    for activity_id in msg.activity_id_list:
        series = ResourceManager.instance().find_by_index(GeneralActivityData, activity_id)
        activity = GeneralActivity(
            general_basic_info=GeneralActivityBasicInfo(
                activity_id=activity_id,
                schedule_id=series.Series if series else 0,
                series_activity_id=[activity_id]
            )
        )
        activity_stage = ResourceManager.instance().find_by_index(GeneralActivityStageGroupData, activity_id)
        if activity_stage:
            activity.activity_stage=GeneralActivityStage(
                stage_group_schedule_list=[
                    GeneralActivityStageGroupScheduleInfo(
                        begin_time=1593223200,
                        end_time=1913140799,
                        stage_group_id=activity_stage.StageGroupID
                    )
                ]
            )
        activity_list.append(activity)

    return GeneralActivityGetMainInfoRsp(
        retcode=0,
        activity_list=activity_list
    )
