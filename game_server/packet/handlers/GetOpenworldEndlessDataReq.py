import betterproto
import random
from game_server.net.session import Session
from game_server.utils import get_unix_in_seconds
from lib.proto import (
    GetOpenworldEndlessDataReq,
    GetOpenworldEndlessDataRsp
)

async def handle(session: Session, msg: GetOpenworldEndlessDataReq) -> betterproto.Message:
    return GetOpenworldEndlessDataRsp(
        retcode=0,
        begin_time=0,
        end_time=int(get_unix_in_seconds() + 3600 * 24 * 7),
        close_time=int(get_unix_in_seconds() + 3600 * 24 * 7 + 1200),
        random_seed=random.randint(1, 1000000),
        hard_level=msg.level,
        type=msg.type
    )
