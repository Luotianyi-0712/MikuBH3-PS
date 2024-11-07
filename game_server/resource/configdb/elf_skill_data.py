from dataclasses import dataclass
from game_server.resource.base_resource import BaseResource
from game_server.resource.decorators import GameResource, LoadPriority

@dataclass
@GameResource("resources/ExcelOutputAsset/ElfSkillData.json", load_priority=LoadPriority.HIGH)
class ElfSkillData(BaseResource):
    ElfSkillID: int
    MaxLv: int
    ElfIds: list
        
    def get_index(self) -> str:
        return str(self.ElfSkillID)
