import betterproto
from game_server.net.session import Session
from game_server.game.enum.data_type import DataType
from database import mongo
from lib.proto import (
    DressEquipmentReq,
    DressEquipmentRsp,
    EquipmentSlot,
    GetAvatarDataReq
)

async def handle(session: Session, msg: DressEquipmentReq) -> betterproto.Message:
    avatar_data = session.player.avatars.get(msg.avatar_id)
    if avatar_data:
        replace_id = 0
        match msg.slot:
            case EquipmentSlot.EQUIPMENT_SLOT_WEAPON_1.value:
                if avatar_data.weapon_id > 0:
                    replace_id = avatar_data.weapon_id
                    replace_weapon = session.player.inventory.weapon_items.get(avatar_data.weapon_id)
                    replace_weapon.equip_avatar_id = 0

                avatar_data.weapon_id = msg.unique_id

                weapon = session.player.inventory.weapon_items.get(msg.unique_id)
                weapon.equip_avatar_id = msg.avatar_id

                mongo.save(session,DataType.WEAPON,[msg.unique_id,replace_id])
            case EquipmentSlot.EQUIPMENT_SLOT_STIGMATA_1.value | \
                EquipmentSlot.EQUIPMENT_SLOT_STIGMATA_2.value | \
                EquipmentSlot.EQUIPMENT_SLOT_STIGMATA_3.value:
                slot_num = msg.slot-1
                replace_id = avatar_data.stigmata_ids.get(slot_num,0)
                if replace_id > 0:
                    replace_stigmata = session.player.inventory.stigmata_items.get(replace_id)
                    replace_stigmata.equip_avatar_id = 0


                avatar_data.stigmata_ids[slot_num] = msg.unique_id
                
                stigmata = session.player.inventory.stigmata_items.get(msg.unique_id)
                stigmata.equip_avatar_id = msg.avatar_id
                stigmata.slot_num = slot_num

                mongo.save(session,DataType.STIGMATA,[msg.unique_id,replace_id])

        await session.process_packet(session.create_packet(GetAvatarDataReq(avatar_id_list=[msg.avatar_id])))
    return DressEquipmentRsp(
        retcode=0,
        unique_id=msg.unique_id,
        slot=msg.slot
    )
