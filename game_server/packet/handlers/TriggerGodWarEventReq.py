import betterproto
import random
from game_server.net.session import Session
from lib.proto import (
    TriggerGodWarEventReq,
    TriggerGodWarEventRsp,
    GodWarEventNotify,
    GodWarEventInfo
)

async def handle(session: Session, msg: TriggerGodWarEventReq) -> betterproto.Message:
    return TriggerGodWarEventRsp(
        retcode=0,
        event_id_list=msg.event_id_list,
        god_war_id=1,
        tale_id=30
    )
