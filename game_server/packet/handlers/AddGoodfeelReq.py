
import betterproto
from game_server.net.session import Session
from lib.proto import AddGoodfeelReq,AddGoodfeelRsp

async def handle(session: Session, msg: AddGoodfeelReq) -> betterproto.Message:
    return AddGoodfeelRsp(retcode=0)
