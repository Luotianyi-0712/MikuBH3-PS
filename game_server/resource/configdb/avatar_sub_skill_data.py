from dataclasses import dataclass
from game_server.resource.base_resource import BaseResource
from game_server.resource.decorators import GameResource

@dataclass
@GameResource("resources/ExcelOutputAsset/AvatarSubSkillData.json")
class AvatarSubSkillData(BaseResource):
    skillId: int
    unlockScoin: int
    maxLv: int
    avatarSubSkillId: int

    def get_index(self) -> str:
        return str(self.avatarSubSkillId)
