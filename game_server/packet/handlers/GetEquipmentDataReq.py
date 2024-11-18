import betterproto
from typing import List
from game_server.net.session import Session
from lib.proto import (
    GetEquipmentDataReq,
    GetEquipmentDataRsp,
    Material,
    Weapon,
    Stigmata,
    StigmataRuneGroup,
    StigmataRune
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
                is_extracted=weapon.is_extracted,
                homology_level=3
            )
            for id, weapon in session.player.inventory.weapon_items.items()
        ],
        stigmata_list=[
            Stigmata(
                unique_id=id,
                id=stigmata.item_id,
                level=stigmata.level,
                exp=stigmata.exp,
                slot_num=2,
                refine_value=stigmata.refine_value,
                promote_times=stigmata.promote_times,
                is_protected=stigmata.is_locked,
                rune_list=[
                    StigmataRune(
                        rune_id=rune.rune_id,
                        strength_percent=rune.strength_percent
                    )
                    for rune in stigmata.rune_list
                ],
                wait_select_rune_group_list=[
                    StigmataRuneGroup(
                        unique_id=index,
                        rune_list=[
                            StigmataRune(
                                rune_id=rune.rune_id,
                                strength_percent=rune.strength_percent
                            )
                            for rune in affix.rune_list
                        ]
                    )
                    for index,affix in enumerate(stigmata.wait_select_rune_group_list, start=1)
                ]
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
