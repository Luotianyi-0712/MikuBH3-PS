from dataclasses import dataclass
from game_server.resource.base_resource import BaseResource
from game_server.resource.decorators import GameResource

@dataclass
@GameResource("resources/ExcelOutputAsset/ActChallengeData.json")
class ActChallengeData(BaseResource):
    actId: int
    difficulty: int

    def get_index(self) -> str:
        return str(self.actId)
