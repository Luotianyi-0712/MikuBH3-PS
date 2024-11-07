import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetOpenworldMechaDefenseReq,
    GetOpenworldMechaDefenseRsp,
    OpenworldMechaDefense
)

async def handle(session: Session, msg: GetOpenworldMechaDefenseReq) -> betterproto.Message:
    return GetOpenworldMechaDefenseRsp(
        retcode=0,
        mecha_defense=OpenworldMechaDefense(
            left_enter_times=1
        )
    )
