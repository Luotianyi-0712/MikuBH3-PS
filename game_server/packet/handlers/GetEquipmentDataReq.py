import betterproto
from typing import List
from game_server.net.session import Session
from game_server.resource import ResourceManager
from game_server.resource.configdb.weapon_data import WeaponData
from game_server.resource.configdb.stigmata_data import StigmataData
from lib.proto import (
    GetEquipmentDataReq,
    GetEquipmentDataRsp,
    Material,
    Weapon,
    Stigmata,
)

async def handle(session: Session, msg: GetEquipmentDataReq) -> betterproto.Message:
    return GetEquipmentDataRsp(
        retcode=0,
        is_all=True,
        weapon_list=[
            Weapon(
                unique_id=id,
                id=weapon.item_id,
                level=weapon.level,
                exp=weapon.exp,
                is_protected=weapon.is_locked,
                is_extracted=weapon.is_extracted
            )
            for id, weapon in session.player.inventory.weapon_items.items()
        ],
        stigmata_list=[
            Stigmata(
                unique_id=id,
                id=stigmata.item_id,
                level=stigmata.level,
                exp=stigmata.exp,
                slot_num=stigmata.slot_num,
                refine_value=stigmata.refine_value,
                promote_times=stigmata.promote_times,
                is_protected=stigmata.is_locked
            )
            for id, stigmata in session.player.inventory.stigmata_items.items()
        ],
        material_list=[
            Material(
                id=material.item_id,
                num=material.num
            )
            for id, material in session.player.inventory.material_items.items()
        ]
    )
