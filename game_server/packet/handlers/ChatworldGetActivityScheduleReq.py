import betterproto
from game_server.net.session import Session
from lib.proto import ChatworldGetActivityScheduleReq, ChatworldGetActivityScheduleRsp

async def handle(session: Session, msg: ChatworldGetActivityScheduleReq) -> betterproto.Message:
    return ChatworldGetActivityScheduleRsp(
        retcode=0,
        scene_id=111
    )
