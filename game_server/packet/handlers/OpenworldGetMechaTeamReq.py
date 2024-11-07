import betterproto
from game_server.net.session import Session
from lib.proto import OpenworldGetMechaTeamReq, OpenworldGetMechaTeamRsp

async def handle(session: Session, msg: OpenworldGetMechaTeamReq) -> betterproto.Message:
    return OpenworldGetMechaTeamRsp(retcode=0)
