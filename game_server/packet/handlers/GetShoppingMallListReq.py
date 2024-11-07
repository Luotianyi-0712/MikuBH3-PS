import betterproto
from game_server.net.session import Session
from lib.proto import GetShoppingMallListReq, GetShoppingMallListRsp

async def handle(session: Session, msg: GetShoppingMallListReq) -> betterproto.Message:
    return GetShoppingMallListRsp(retcode=0)
