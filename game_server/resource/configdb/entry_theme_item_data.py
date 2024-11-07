from dataclasses import dataclass
from game_server.resource.base_resource import BaseResource
from game_server.resource.decorators import GameResource

@dataclass
@GameResource("resources/ExcelOutputAsset/EntryThemeItemData.json")
class EntryThemeItemData(BaseResource):
    ThemeItemID: int

    def get_index(self) -> str:
        return str(self.ThemeItemID)
