import betterproto
from game_server.net.session import Session
from lib.proto import SyncTimeReq, SyncTimeRsp
from utils.time import get_unix_in_seconds


async def handle(session: Session, msg: SyncTimeReq) -> betterproto.Message:
    return SyncTimeRsp(retcode=0, cur_time=get_unix_in_seconds(), seq=msg.seq)
