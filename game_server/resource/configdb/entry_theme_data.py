from dataclasses import dataclass
from game_server.resource.base_resource import BaseResource
from game_server.resource.decorators import GameResource

@dataclass
@GameResource("resources/ExcelOutputAsset/EntryThemeData.json")
class EntryThemeData(BaseResource):
    SpaceShipConfigID: int
    ThemeBGMConfigList: list
    ThemeTagList: list

    def get_index(self) -> str:
        return str(self.SpaceShipConfigID)
