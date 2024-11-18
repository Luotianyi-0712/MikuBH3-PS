import betterproto
import random
from game_server.net.session import Session
from game_server.resource import ResourceManager
from game_server.resource.configdb.affix_list import AffixListData
from game_server.game.inventory.inventory_manager import RuneList,RuneGroup
from lib.proto import (
    RefineStigmataRuneReq,
    RefineStigmataRuneRsp,
    StigmataRuneGroup,
    StigmataRune,
    StigmataRefineTimesType,
    GetEquipmentDataReq
)

def generate_affix_and_percentage(affix_ids):
    affix_id1, affix_id2 = random.choice(affix_ids), random.choice(affix_ids)
    percentage1, percentage2 = [
        random.randint(*r) for r in random.choices(
            [(20, 50), (50, 70), (80, 100)], weights=[50, 40, 10], k=2
        )
    ]
    return {"affix1": affix_id1, "percentage1": percentage1, "affix2": affix_id2, "percentage2": percentage2}

async def handle(session: Session, msg: RefineStigmataRuneReq) -> betterproto.Message:
    stigmata_data = session.player.inventory.stigmata_items.get(msg.unique_id)
    affix_ids = [affix.affixID for affix in ResourceManager.instance().values(AffixListData)]
    result = []
    if msg.times_type == StigmataRefineTimesType.STIGMATA_REFINE_TIMES_TEN.value:
        result = [generate_affix_and_percentage(affix_ids) for _ in range(10)]
    else:
        result.append(generate_affix_and_percentage(affix_ids))
    stigmata_data.wait_select_rune_group_list = []
    stigmata_data.wait_select_rune_group_list.extend(
        [
            RuneGroup(
                unique_id=index,
                rune_list=[
                    RuneList(
                        rune_id=affix['affix1'],
                        strength_percent=affix['percentage1']
                    ),
                    RuneList(
                        rune_id=affix['affix2'],
                        strength_percent=affix['percentage2']
                    )
                ]
            )
            for index, affix in enumerate(result, start=1)
        ]
    )

    await session.process_packet(session.create_packet(GetEquipmentDataReq()))

    return RefineStigmataRuneRsp(
        retcode=0,
        rune_group_list=[
            StigmataRuneGroup(
                unique_id=index,
                rune_list=[
                    StigmataRune(
                        rune_id=affix['affix1'],
                        strength_percent=affix['percentage1']
                    ),
                    StigmataRune(
                        rune_id=affix['affix2'],
                        strength_percent=affix['percentage2']
                    ),
                ]
            )
            for index, affix in enumerate(result, start=1)
        ],
        times_type=10 if msg.times_type > 0 else 1
    )
