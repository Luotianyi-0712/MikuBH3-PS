from dataclasses import dataclass
from game_server.resource.base_resource import BaseResource
from game_server.resource.decorators import GameResource

@dataclass
@GameResource("resources/ExcelOutputAsset/RecommendPanel.json")
class RecommendPanelData(BaseResource):
    PanelID: int

    def get_index(self) -> str:
        return str(self.PanelID)
