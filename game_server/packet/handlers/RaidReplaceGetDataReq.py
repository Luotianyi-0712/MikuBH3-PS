import betterproto
from game_server.net.session import Session
from lib.proto import (
    RaidReplaceGetDataReq,
    RaidReplaceGetDataRsp,
    RaidReplaceActivity
)

async def handle(session: Session, msg: RaidReplaceGetDataReq) -> betterproto.Message:
    return RaidReplaceGetDataRsp(
        retcode=0,
        activity_list=[
            RaidReplaceActivity(
                activity_id=7042,
                opened_stage_list=[
                    431016,
                    431020,
                    432013,
                    433024,
                    433027,
                    434003,
                    436016
                ],
                reward_line_id=30001
            )
        ],
        schedule_id=7005
    )
