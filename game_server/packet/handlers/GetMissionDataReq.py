import betterproto
from game_server.net.session import Session
from game_server.resource import ResourceManager
from game_server.resource.configdb.mission_data import MissionData
from utils.time import get_unix_in_seconds
from lib.proto import (
    GetMissionDataReq,
    GetMissionDataRsp,
    Mission,
    MissionStatus,
    ChallengeMissionData,
    MainlineStepMission,
)


async def handle(session: Session, msg: GetMissionDataReq) -> betterproto.Message:
    return GetMissionDataRsp(
        retcode=0,
        challenge_mission=ChallengeMissionData(is_unlock=True),
        close_mission_list=[
            mission.id for mission in ResourceManager.instance().values(MissionData)
        ],
        is_all=True,
        is_in_activity=True,
        mainline_step=MainlineStepMission(is_update=True),
        mission_list=[
            Mission(
                mission_id=mission.id,
                status=MissionStatus.MISSION_CLOSE.value,
                priority=mission.Priority,
                progress=mission.totalProgress,
                begin_time=0,
                end_time=2073239999,
                cycle_id=1,
            )
            for mission in ResourceManager.instance().values(MissionData)
        ],
    )
