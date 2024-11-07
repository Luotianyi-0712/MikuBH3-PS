import betterproto
from game_server.net.session import Session
from lib.proto import OpenworldHuntActivityGetDataReq,OpenworldHuntActivityGetDataRsp

async def handle(session: Session, msg: OpenworldHuntActivityGetDataReq) -> betterproto.Message:
    return OpenworldHuntActivityGetDataRsp(retcode=0)
