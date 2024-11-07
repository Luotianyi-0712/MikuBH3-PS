import dataclasses
from typing import List
from lib.proto import AvatarSubSkill

@dataclasses.dataclass
class Skill:
    skill_id : int
    sub_skill_lists : dict[int, AvatarSubSkill] = dataclasses.field(default_factory=dict)

@dataclasses.dataclass
class AvatarManager:
    avatar_id: int
    star: int
    level: int
    exp: int
    fragment: List
    touch_good_feel: List
    today_has_add_good_feel: int
    dress_id: int
    dress_lists: List
    sub_star: int
    skill_lists: dict[int, Skill]
    weapon_id: int = 0
    stigmata_ids: dict = dataclasses.field(default_factory=dict)

@dataclasses.dataclass
class AvatarTeamManager:
    team_id: int
    name: str
    astral_mate_id: int
    is_using_astra_mate: bool
    elf_id_list: List
    avatar_id_list: List
