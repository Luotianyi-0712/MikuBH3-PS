import betterproto
from game_server.net.session import Session
from lib.proto import EnterWorldChatroomReq, EnterWorldChatroomRsp

async def handle(session: Session, msg: EnterWorldChatroomReq) -> betterproto.Message:
    return EnterWorldChatroomRsp(
        retcode=0,
        chatroom_id=1,
        player_num=69
    )
