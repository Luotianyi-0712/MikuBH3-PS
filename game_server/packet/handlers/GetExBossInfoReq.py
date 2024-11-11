import betterproto
import json
from game_server.net.session import Session
from lib.proto import (
    GetExBossInfoReq,
    GetExBossInfoRsp,
    ExBossInfo,
    ExBossIdInfo
)

async def handle(session: Session, msg: GetExBossInfoReq) -> betterproto.Message:
    with open("Battle.json", "r") as file:
        data = json.load(file)
    return GetExBossInfoRsp(
        retcode=0,
        boss_info=ExBossInfo(
            boss_id_list=[
                ExBossIdInfo(
                    boss_id=id
                )
                for id in data.get("memo", {}).get("boss_ids", [])
            ],
            cur_max_enter_times=18,
            rank_id=104,
            schedule_id=10377,
            now_schedule_id=10377
        )
    )
