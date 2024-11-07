import betterproto
from game_server.net.session import Session
from lib.proto import GetExtractReforgeActivityReq,GetExtractReforgeActivityRsp

async def handle(session: Session, msg: GetExtractReforgeActivityReq) -> betterproto.Message:
    return GetExtractReforgeActivityRsp(retcode=0)
