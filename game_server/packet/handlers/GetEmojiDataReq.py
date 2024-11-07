import betterproto
from game_server.net.session import Session
from lib.proto import GetEmojiDataReq, GetEmojiDataRsp

async def handle(session: Session, msg: GetEmojiDataReq) -> betterproto.Message:
    return GetEmojiDataRsp(retcode=0,is_all=True)
