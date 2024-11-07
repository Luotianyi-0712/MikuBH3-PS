from dataclasses import dataclass
from game_server.resource.base_resource import BaseResource
from game_server.resource.decorators import GameResource

@dataclass
@GameResource("resources/ExcelOutputAsset/MissionData.json")
class MissionData(BaseResource):
    id: int
    Priority: int
    totalProgress: int

    def get_index(self) -> str:
        return str(self.id)
