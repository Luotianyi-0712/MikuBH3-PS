import betterproto
from game_server.net.session import Session
from lib.proto import GetPlayerTokenReq,GetPlayerTokenRsp

async def handle(session: Session, msg: GetPlayerTokenReq) -> betterproto.Message:
    return GetPlayerTokenRsp(
        retcode=0,
        uid=1337,
        token=msg.token,
        account_type=msg.account_type,
        account_uid="1337",
        user_type=4,
        hoyolab_account_uid="1337",
        fightserver_ip=0,
        fightserver_port=0
    )
