import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetExBossInfoReq,
    GetExBossInfoRsp,
    ExBossInfo,
    ExBossIdInfo
)

async def handle(session: Session, msg: GetExBossInfoReq) -> betterproto.Message:
    return GetExBossInfoRsp(
        retcode=0,
        boss_info=ExBossInfo(
            boss_id_list=[
                ExBossIdInfo(
                    boss_id=48016
                ),
                ExBossIdInfo(
                    boss_id=41021
                ),
                ExBossIdInfo(
                    boss_id=13021
                )
            ],
            cur_max_enter_times=714,
            rank_id=104,
            schedule_id=10359
        )
    )
