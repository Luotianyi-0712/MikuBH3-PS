from dataclasses import dataclass
from game_server.resource.base_resource import BaseResource
from game_server.resource.decorators import GameResource

@dataclass
@GameResource("resources/ExcelOutputAsset/ThemeData_Avatar.json")
class ThemeDataAvatar(BaseResource):
    AvatarData: int
    BuffList: list[int]
    avatarIDList: list[int]

    def get_index(self) -> str:
        return str(self.AvatarData)
