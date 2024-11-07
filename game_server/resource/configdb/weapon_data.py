from dataclasses import dataclass
from game_server.resource.base_resource import BaseResource
from game_server.resource.decorators import GameResource

@dataclass
@GameResource("resources/ExcelOutputAsset/WeaponData.json")
class WeaponData(BaseResource):
    ID: int
    weaponMainID: int
    maxLv: int
    rarity: int
    maxRarity: int
    evoID: int
    protect: bool

    def get_index(self) -> str:
        return str(self.ID)
