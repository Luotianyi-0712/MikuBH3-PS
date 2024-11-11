import betterproto
import random
from game_server.net.session import Session
from lib.proto import (
    GodWarEventNotify,
    GodWarEventInfo
)

async def handle(session: Session, msg: GodWarEventNotify) -> betterproto.Message:
    return GodWarEventNotify(
        god_war_id=1,
        tale_id=30,
        event_list=[
            GodWarEventInfo(
                event_id=570018,
                event_param_list=[
                    418,
                    0
                ],
                event_type=33,
                source_event_id=57000,
                source_type=1
            ),
            GodWarEventInfo(
                event_id=3000045,
                event_type=10,
                source_event_id=5910000,
                source_type=1
            ),
            GodWarEventInfo(
                event_id=5910000,
                event_type=99,
                source_event_id=57000,
                source_type=1
            ),
            GodWarEventInfo(
                event_id=3000045,
                event_type=10,
                source_event_id=570000,
                source_type=1
            ),
            GodWarEventInfo(
                event_id=5600145,
                event_param_list=[
                    10,
                    718,
                    1
                ],
                event_type=49,
                source_event_id=570000,
                source_type=1
            ),
            GodWarEventInfo(
                event_id=570000,
                event_type=99,
                source_event_id=57000,
                source_type=1
            ),
            GodWarEventInfo(
                event_id=57000,
                event_type=99,
                source_event_id=57000,
                source_type=1
            )
        ]
    )
