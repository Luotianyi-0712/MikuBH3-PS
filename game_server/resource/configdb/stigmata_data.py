from dataclasses import dataclass
from game_server.resource.base_resource import BaseResource
from game_server.resource.decorators import GameResource

@dataclass
@GameResource("resources/ExcelOutputAsset/StigmataData.json")
class StigmataData(BaseResource):
    ID: int
    maxLv: int
    rarity: int
    maxRarity: int
    evoID: int
    quality: int
    isSecurityProtect: bool
    protect: bool

    def on_load(self) -> bool:
       return self.evoID == 0

    def get_index(self) -> str:
        return str(self.ID)
