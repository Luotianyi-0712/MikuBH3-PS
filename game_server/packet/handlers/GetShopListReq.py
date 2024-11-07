import betterproto
from game_server.net.session import Session
from lib.proto import GetShopListReq,GetShopListRsp

async def handle(session: Session, msg: GetShopListReq) -> betterproto.Message:
    return GetShopListRsp(
        retcode=0,
        is_all=True
    )
