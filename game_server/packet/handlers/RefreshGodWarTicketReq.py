import betterproto
from game_server.net.session import Session
from lib.proto import (RefreshGodWarTicketReq,RefreshGodWarTicketRsp)

async def handle(session: Session, msg: RefreshGodWarTicketReq) -> betterproto.Message:
    return RefreshGodWarTicketRsp(
        retcode=0,
        god_war_id=msg.god_war_id
    )