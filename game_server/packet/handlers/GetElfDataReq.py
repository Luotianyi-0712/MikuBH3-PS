import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetElfDataReq,
    GetElfDataRsp,
    Elf,
    ElfSkill
)

async def handle(session: Session, msg: GetElfDataReq) -> betterproto.Message:
    return GetElfDataRsp(
        retcode=0,
        elf_list=[
            Elf(
                elf_id=elf_id,
                level=elf.level,
                star=elf.star,
                exp=elf.exp,
                skill_list=[
                    ElfSkill(
                        skill_id=skill_id,
                        skill_level=skill.level
                    )
                    for skill_id,skill in elf.skill_list.items()
                ]
            )
            for elf_id,elf in session.player.elfs.items()
        ]
    )
