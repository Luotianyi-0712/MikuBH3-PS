import betterproto
from game_server.net.session import Session
from game_server.game.enum.data_type import DataType
from database import mongo
from lib.proto import (
    SetWarshipReq,
    SetWarshipRsp,
    GetMainDataRsp,
    WarshipThemeData
)

async def handle(session: Session, msg: SetWarshipReq) -> betterproto.Message:
    await session.send(session.create_packet(
            GetMainDataRsp(
                retcode=0,
                warship_theme=WarshipThemeData(
                    warship_id=msg.warship_id
                ),
                type_list=[35]
            )
        )
    )
    session.player.warship_id = msg.warship_id
    mongo.save(session,DataType.PLAYER)
    return SetWarshipRsp(retcode=0)
