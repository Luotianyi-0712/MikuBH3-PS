import betterproto
from game_server.net.session import Session
from lib.proto import GetChapterActivityDataReq,GetChapterActivityDataRsp

async def handle(session: Session, msg: GetChapterActivityDataReq) -> betterproto.Message:
    return GetChapterActivityDataRsp(retcode=0)
