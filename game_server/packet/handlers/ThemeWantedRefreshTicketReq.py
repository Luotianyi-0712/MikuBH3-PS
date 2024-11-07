import betterproto
from game_server.net.session import Session
from lib.proto import ThemeWantedRefreshTicketReq, ThemeWantedRefreshTicketRsp

async def handle(session: Session, msg: ThemeWantedRefreshTicketReq) -> betterproto.Message:
    return ThemeWantedRefreshTicketRsp(retcode=0)
