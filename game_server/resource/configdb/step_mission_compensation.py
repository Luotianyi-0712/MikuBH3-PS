from dataclasses import dataclass
from game_server.resource.base_resource import BaseResource
from game_server.resource.decorators import GameResource

@dataclass
@GameResource("resources/ExcelOutputAsset/StepMissionCompensation.json")
class StepMissionCompensationData(BaseResource):
    CompensationID: int
    UnlockLevel: int
    MainLineStepIDList: list
    NewChallengeStepIDList: list
    OldChallengeStepIDList: list

    def get_index(self) -> str:
        return str(self.CompensationID)
