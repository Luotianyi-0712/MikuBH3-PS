import betterproto
from game_server.net.session import Session
from lib.proto import GetChapterCompensationInfoReq,GetChapterCompensationInfoRsp

async def handle(session: Session, msg: GetChapterCompensationInfoReq) -> betterproto.Message:
    return GetChapterCompensationInfoRsp(retcode=0)
