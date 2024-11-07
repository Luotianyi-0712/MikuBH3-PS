import betterproto
from game_server.net.session import Session
from lib.proto import GetStageChapterReq,GetStageChapterRsp

async def handle(session: Session, msg: GetStageChapterReq) -> betterproto.Message:
    return GetStageChapterRsp(retcode=0)
