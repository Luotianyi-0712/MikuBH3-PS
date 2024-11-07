import betterproto
from game_server.net.session import Session
from lib.proto import GetMissionGroupMainInfoReq,GetMissionGroupMainInfoRsp

async def handle(session: Session, msg: GetMissionGroupMainInfoReq) -> betterproto.Message:
    return GetMissionGroupMainInfoRsp(
        retcode=0,
        has_take_reward_mission_group_list=[97001]
    )
