from dataclasses import dataclass
from game_server.resource.base_resource import BaseResource
from game_server.resource.decorators import GameResource

@dataclass
@GameResource("resources/ExcelOutputAsset/StageData_Main.json")
class StageDataMain(BaseResource):
    levelId: int
    maxProgress: int
    challengeList: list

    def get_index(self) -> str:
        return str(self.levelId)
