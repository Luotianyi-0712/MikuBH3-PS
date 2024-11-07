import betterproto
import random
from game_server.net.session import Session
from lib.proto import (UltraEndlessReportSiteFloorReq,UltraEndlessReportSiteFloorRsp,)

async def handle(session: Session, msg: UltraEndlessReportSiteFloorReq) -> betterproto.Message:
    return UltraEndlessReportSiteFloorRsp(
        retcode=0,
        floor=msg.floor,
        site_id=msg.site_id
    )
    
