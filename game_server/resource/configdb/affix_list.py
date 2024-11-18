from dataclasses import dataclass
from game_server.resource.base_resource import BaseResource
from game_server.resource.decorators import GameResource

@dataclass
@GameResource("resources/ExcelOutputAsset/AffixList.json")
class AffixListData(BaseResource):
    affixID: int
    level: int

    def on_load(self) -> bool:
        return self.level == 3

    def get_index(self) -> str:
        return str(self.affixID)
