import betterproto
from game_server.net.session import Session
from lib.proto import GetClientSettingReq,GetClientSettingRsp

async def handle(session: Session, msg: GetClientSettingReq) -> betterproto.Message:
    return GetClientSettingRsp(
        retcode=0,
        client_setting_type=msg.client_setting_type,
        is_weekly_guide_switch_on=True,
        avatar_artifact_switch_list=[]
    )
