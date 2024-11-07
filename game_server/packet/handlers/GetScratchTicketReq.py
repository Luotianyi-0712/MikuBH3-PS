import betterproto
from game_server.net.session import Session
from lib.proto import GetScratchTicketReq,GetScratchTicketRsp

async def handle(session: Session, msg: GetScratchTicketReq) -> betterproto.Message:
    return GetScratchTicketRsp(retcode=0)
