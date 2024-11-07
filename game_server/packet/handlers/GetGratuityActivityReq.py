import betterproto
from game_server.net.session import Session
from lib.proto import GetGratuityActivityReq,GetGratuityActivityRsp

async def handle(session: Session, msg: GetGratuityActivityReq) -> betterproto.Message:
    return GetGratuityActivityRsp(retcode=0)
