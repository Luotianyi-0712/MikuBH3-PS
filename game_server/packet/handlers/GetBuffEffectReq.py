
import betterproto
from game_server.net.session import Session
from game_server.utils import get_unix_in_seconds
from lib.proto import (
    GetBuffEffectReq,
    GetBuffEffectRsp,
    BuffEffect
)

async def handle(session: Session, msg: GetBuffEffectReq) -> betterproto.Message:
    return GetBuffEffectRsp(
        retcode=0,
        effect_list=[
            BuffEffect(
                effect_id=i,
                end_time=int(get_unix_in_seconds()+3600*24*7)
            )
            for i in msg.effect_id_list
        ],
        aura_effect_list=msg.effect_id_list[:]
    )
