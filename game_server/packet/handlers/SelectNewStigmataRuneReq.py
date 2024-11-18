
import betterproto
from game_server.net.session import Session
from game_server.game.inventory.inventory_manager import RuneList
from game_server.game.enum.data_type import DataType
from database import mongo
from lib.proto import (
    SelectNewStigmataRuneReq,
    SelectNewStigmataRuneRsp,
    GetEquipmentDataReq
)

async def handle(session: Session, msg: SelectNewStigmataRuneReq) -> betterproto.Message:
    stigmata_data = session.player.inventory.stigmata_items.get(msg.unique_id)

    if msg.select_unique_id > 0 and msg.is_select:
        affix_data = [affix for affix in stigmata_data.wait_select_rune_group_list if msg.select_unique_id == affix.unique_id][0]
        stigmata_data.rune_list = []
        stigmata_data.rune_list.extend(
            [
                RuneList(
                    rune_id=rune.rune_id,
                    strength_percent=rune.strength_percent
                )
                for rune in affix_data.rune_list
            ]
        )
        mongo.save(session,DataType.STIGMATA,[msg.unique_id])

    stigmata_data.wait_select_rune_group_list = []
    await session.process_packet(session.create_packet(GetEquipmentDataReq()))

    return SelectNewStigmataRuneRsp(
        retcode=0,
        select_unique_id=msg.select_unique_id,
        is_select=msg.is_select
    )
        
