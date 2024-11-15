import betterproto
from game_server.net.session import Session
from lib.proto import (
    PjmsGetChapterDataReq,
    PjmsGetChapterDataRsp,
    PjmsChapter,
    ChapterShadowLake,
    PjmsFormation,
    PjmsUnitInfo,
    PjmsAuxiliaryUnit,
    PjmsCoreUnit,
    PjmsUnitSet,
    PjmsUnitSetSlot
)

async def handle(session: Session, msg: PjmsGetChapterDataReq) -> betterproto.Message:
    return PjmsGetChapterDataRsp(
        retcode=0,
        is_all=True,
        cur_chapter_id=100,
        chapter_list=[
            PjmsChapter(
                chapter_id=100,
                chapter_shadowlake=ChapterShadowLake(
                    energy_num=2,
                    max_energy_num=5
                ),
                cur_track_series_id=1022,
                exp=530,
                formation=[
                    PjmsFormation(
                        avatar_id_list=[150],
                        elf_id=4224,
                        is_elf_mode=True
                    )
                ],
                last_take_chapter_reward_level=7,
                last_take_chapter_reward_material_num=1000,
                level=7,
                playing_bgm_id=19,
                talent_level=7,
                unit_info=PjmsUnitInfo(
                    auxiliary_unit_list=[
                        PjmsAuxiliaryUnit(
                            exp=170,
                            level=2,
                            unique_id=1000,
                            unit_id=301
                        ),
                        PjmsAuxiliaryUnit(
                            level=1,
                            unique_id=101,
                            unit_id=301
                        ),
                        PjmsAuxiliaryUnit(
                            exp=10,
                            level=2,
                            unique_id=1002,
                            unit_id=201
                        ),
                        PjmsAuxiliaryUnit(
                            level=1,
                            unique_id=1003,
                            unit_id=205
                        ),
                        PjmsAuxiliaryUnit(
                            level=1,
                            unique_id=1004,
                            unit_id=302
                        ),
                        PjmsAuxiliaryUnit(
                            level=1,
                            unique_id=1005,
                            unit_id=302
                        ),
                        PjmsAuxiliaryUnit(
                            level=1,
                            unique_id=1006,
                            unit_id=303
                        ),
                        PjmsAuxiliaryUnit(
                            level=1,
                            unique_id=1007,
                            unit_id=207
                        ),
                        PjmsAuxiliaryUnit(
                            level=1,
                            unique_id=1008,
                            unit_id=303
                        ),
                    ],
                    core_unit_list=[
                        PjmsCoreUnit(
                            level=1,
                            unit_id=1
                        ),
                        PjmsCoreUnit(
                            level=2,
                            unit_id=2
                        ),
                        PjmsCoreUnit(
                            level=1,
                            unit_id=3
                        ),
                    ],
                    cur_unit_set_id=1,
                    unit_set_list=[
                        PjmsUnitSet(
                            set_id=1,
                            slot_list=[
                                PjmsUnitSetSlot(
                                    id=2,
                                    slot_id=10
                                ),
                                PjmsUnitSetSlot(
                                    id=1002,
                                    slot_id=100
                                ),
                                PjmsUnitSetSlot(
                                    id=1004,
                                    slot_id=110
                                ),
                                PjmsUnitSetSlot(
                                    id=1006,
                                    slot_id=120
                                )
                            ]
                        ),
                        PjmsUnitSet(
                            set_id=2
                        ),
                        PjmsUnitSet(
                            set_id=3
                        ),
                        PjmsUnitSet(
                            set_id=4
                        ),
                        PjmsUnitSet(
                            set_id=5
                        )
                    ]
                )
            )
        ]
    )
