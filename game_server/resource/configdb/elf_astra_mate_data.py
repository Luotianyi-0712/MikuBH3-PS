from dataclasses import dataclass
from game_server.resource.base_resource import BaseResource
from game_server.resource.configdb.elf_skill_data import ElfSkillData
from game_server.resource.decorators import GameResource

@dataclass
@GameResource("resources/ExcelOutputAsset/Elf_AstraMate_Data.json")
class ElfAstraMateData(BaseResource):
    ElfID: int
    MaxLevel: int
    MaxRarity: int
    
    skill_lists: list[ElfSkillData]

    def on_load(self) -> bool:
        from game_server.resource import ResourceManager

        self.skill_lists = [
            skill
            for skill in ResourceManager.instance().values(ElfSkillData)
            if self.ElfID in skill.ElfIds
        ]
        return True

    def get_index(self) -> str:
        return str(self.ElfID)
