import betterproto
import random
from game_server.net.session import Session
from lib.proto import GetGalInteractTriggerEventReq,GetGalInteractTriggerEventRsp

async def handle(session: Session, msg: GetGalInteractTriggerEventReq) -> betterproto.Message:
    return GetGalInteractTriggerEventRsp(
        retcode=0,
        avatar_id=msg.avatar_id,
        event_id=0
    )
