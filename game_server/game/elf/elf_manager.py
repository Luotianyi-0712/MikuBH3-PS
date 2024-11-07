import dataclasses
from typing import List

@dataclasses.dataclass
class ElfSkill:
    skill_id: int
    level: int

@dataclasses.dataclass
class ElfManager:
    elf_id: int
    level: int
    star: int
    exp: 0
    skill_list: dict[int,ElfSkill] = dataclasses.field(default_factory=dict)

