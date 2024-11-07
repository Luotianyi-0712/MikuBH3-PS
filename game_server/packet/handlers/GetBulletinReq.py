import betterproto
from game_server.net.session import Session
from lib.proto import GetBulletinReq,GetBulletinRsp

async def handle(session: Session, msg: GetBulletinReq) -> betterproto.Message:
    return GetBulletinRsp(
        retcode=0,
        is_all=True
    )
