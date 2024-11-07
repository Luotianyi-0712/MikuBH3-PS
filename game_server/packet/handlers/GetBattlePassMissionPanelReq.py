import betterproto
from game_server.net.session import Session
from lib.proto import GetBattlePassMissionPanelReq,GetBattlePassMissionPanelRsp

async def handle(session: Session, msg: GetBattlePassMissionPanelReq) -> betterproto.Message:
    return GetBattlePassMissionPanelRsp(retcode=0)
