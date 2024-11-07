import betterproto
from game_server.net.session import Session
from lib.proto import GetTradingCardActivityReq, GetTradingCardActivityRsp

async def handle(session: Session, msg: GetTradingCardActivityReq) -> betterproto.Message:
    return GetTradingCardActivityRsp(retcode=0)
