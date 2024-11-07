import betterproto
from game_server.net.session import Session
from lib.proto import UpdateMissionProgressReq,UpdateMissionProgressRsp

async def handle(session: Session, msg: UpdateMissionProgressReq) -> betterproto.Message:
    return UpdateMissionProgressRsp(retcode=0)
