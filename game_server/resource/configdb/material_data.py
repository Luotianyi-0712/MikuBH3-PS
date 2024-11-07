from dataclasses import dataclass
from game_server.resource.base_resource import BaseResource
from game_server.resource.decorators import GameResource

@dataclass
@GameResource("resources/ExcelOutputAsset/MaterialData.json")
class MaterialData(BaseResource):
    ID: int
    rarity: int
    maxRarity: int
    quantityLimit: int

    def get_index(self) -> str:
        return str(self.ID)
