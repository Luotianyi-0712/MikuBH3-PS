import betterproto
from game_server.net.session import Session
from game_server.game.enum.data_type import DataType
from database import mongo
from lib.proto import SetDressReq,SetDressRsp

async def handle(session: Session, msg: SetDressReq) -> betterproto.Message:
    avatar = session.player.avatars.get(msg.avatar_id)
    avatar.dress_id = msg.dress_id
    mongo.save(session,DataType.AVATAR,[msg.avatar_id])
    return SetDressRsp(retcode=0)
