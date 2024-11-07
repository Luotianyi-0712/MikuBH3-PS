import betterproto
from game_server.net.session import Session
from lib.proto import GetRaffleActivityReq,GetRaffleActivityRsp

async def handle(session: Session, msg: GetRaffleActivityReq) -> betterproto.Message:
    return GetRaffleActivityRsp(retcode=0)
