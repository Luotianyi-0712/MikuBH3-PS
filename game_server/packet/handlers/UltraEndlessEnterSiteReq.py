import betterproto
import random
from game_server.net.session import Session
from lib.proto import (
    UltraEndlessEnterSiteReq,
    UltraEndlessEnterSiteRsp,
)

async def handle(session: Session, msg: UltraEndlessEnterSiteReq) -> betterproto.Message:
    return UltraEndlessEnterSiteRsp(
        retcode=0,
        site_id=msg.site_id
    )
