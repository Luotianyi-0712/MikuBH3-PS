import betterproto
from game_server.net.session import Session
from lib.proto import SanctuaryGetMainInfoReq, SanctuaryGetMainInfoRsp

async def handle(session: Session, msg: SanctuaryGetMainInfoReq) -> betterproto.Message:
    return SanctuaryGetMainInfoRsp(retcode=0)
