import betterproto
from game_server.net.session import Session
from lib.proto import GetAuthkeyReq,GetAuthkeyRsp

async def handle(session: Session, msg: GetAuthkeyReq) -> betterproto.Message:
    return GetAuthkeyRsp(
        retcode=0,
        auth_appid=msg.auth_appid,
        authkey="0",
        sign_type=2,
        authkey_ver=1
    )
