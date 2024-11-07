import betterproto
from game_server.net.session import Session
from lib.proto import GetMissionThemeDataReq, GetMissionThemeDataRsp

async def handle(session: Session, msg: GetMissionThemeDataReq) -> betterproto.Message:
    return GetMissionThemeDataRsp(retcode=0,is_get_all=True)
