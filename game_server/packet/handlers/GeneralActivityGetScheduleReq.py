import betterproto
from game_server.net.session import Session
from game_server.resource import ResourceManager
from game_server.resource.configdb.avatar_tutorial import AvatarTutorialData
from game_server.resource.configdb.activity_tower import ActivityTowerData
from game_server.utils import get_unix_in_seconds
from lib.proto import (
    GeneralActivityGetScheduleReq,
    GeneralActivityGetScheduleRsp,
    GeneralActivityScheduleInfo
)

async def handle(session: Session, msg: GeneralActivityGetScheduleReq) -> betterproto.Message:

    schedule_list = []

    for tutorial in ResourceManager.instance().values(AvatarTutorialData):
        schedule_list.append(
            GeneralActivityScheduleInfo(
                activity_id=tutorial.ActivityID,
                settle_time=int(get_unix_in_seconds()+3600*24*7),
                end_time=int(get_unix_in_seconds()+3600*24*7),
                end_day_time=int(get_unix_in_seconds()+3600*24*7)
            )
        )

    for tower in ResourceManager.instance().values(ActivityTowerData):
        schedule_list.append(
            GeneralActivityScheduleInfo(
                activity_id=tower.ActivityID,
                settle_time=int(get_unix_in_seconds()+3600*24*7),
                end_time=int(get_unix_in_seconds()+3600*24*7),
                end_day_time=int(get_unix_in_seconds()+3600*24*7)
            )
        )

    return GeneralActivityGetScheduleRsp(
        retcode=0,
        schedule_list=schedule_list
    )
