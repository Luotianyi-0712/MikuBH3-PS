import betterproto
from game_server.net.session import Session
from lib.proto import GetCurrencyExchangeInfoReq, GetCurrencyExchangeInfoRsp

async def handle(session: Session, msg: GetCurrencyExchangeInfoReq) -> betterproto.Message:
    return GetCurrencyExchangeInfoRsp(retcode=0)
