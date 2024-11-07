from dataclasses import dataclass
from game_server.resource.base_resource import BaseResource
from game_server.resource.decorators import GameResource

@dataclass
@GameResource("resources/ExcelOutputAsset/DressData.json")
class DressData(BaseResource):
    dressID: int
    avatarIDList: list

    def get_index(self) -> str:
        return str(self.dressID)
