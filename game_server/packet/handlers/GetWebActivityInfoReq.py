import betterproto
from game_server.net.session import Session
from lib.proto import GetWebActivityInfoReq,GetWebActivityInfoRsp

async def handle(session: Session, msg: GetWebActivityInfoReq) -> betterproto.Message:
    return GetWebActivityInfoRsp(
        retcode=0,
        web_activity_list=[]
    )
