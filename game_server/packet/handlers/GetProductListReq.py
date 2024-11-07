import betterproto
from game_server.net.session import Session
from game_server.utils import get_unix_in_seconds
from lib.proto import GetProductListReq,GetProductListRsp

async def handle(session: Session, msg: GetProductListReq) -> betterproto.Message:
    return GetProductListRsp(
        retcode=0,
        next_random_box_product_refresh_time=int(get_unix_in_seconds() + 3600 * 24),
        next_limit_product_refresh_time=int(get_unix_in_seconds() + 3600 * 24)
    )
