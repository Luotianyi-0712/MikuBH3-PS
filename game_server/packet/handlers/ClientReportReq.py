import betterproto
from game_server.net.session import Session
from lib.proto import ClientReportReq,ClientReportRsp

async def handle(session: Session, msg: ClientReportReq) -> betterproto.Message:
    return ClientReportRsp(retcode=0)
