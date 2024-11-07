import betterproto
import random
from game_server.net.session import Session
from lib.proto import TakeGalInteractTriggerEventReq,TakeGalInteractTriggerEventRsp

async def handle(session: Session, msg: TakeGalInteractTriggerEventReq) -> betterproto.Message:
    return TakeGalInteractTriggerEventRsp(
        retcode=0,
        avatar_id=msg.avatar_id,
        event_id=msg.event_id
    )
