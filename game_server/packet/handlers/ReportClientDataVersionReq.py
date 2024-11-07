import betterproto
from game_server.net.session import Session
from lib.proto import ReportClientDataVersionReq,ReportClientDataVersionRsp

async def handle(session: Session, msg: ReportClientDataVersionReq) -> betterproto.Message:
    return ReportClientDataVersionRsp(server_version=msg.version)
