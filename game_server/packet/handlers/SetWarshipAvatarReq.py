import betterproto
from game_server.net.session import Session
from game_server.game.enum.data_type import DataType
from database import mongo
from lib.proto import (
    SetWarshipAvatarReq,
    SetWarshipAvatarRsp,
    GetMainDataRsp,
    WarshipAvatarData
)

async def handle(session: Session, msg: SetWarshipAvatarReq) -> betterproto.Message:
    await session.send(session.create_packet(
            GetMainDataRsp(
                retcode=0,
                warship_avatar=WarshipAvatarData(
                    warship_first_avatar_id=msg.first_avatar_id,
                    warship_second_avatar_id=0
                ),
                type_list=[35]
            )
        )
    )
    session.player.warship_avatar.warship_first_avatar_id = msg.first_avatar_id
    mongo.save(session,DataType.PLAYER)
    return SetWarshipAvatarRsp(retcode=0)
