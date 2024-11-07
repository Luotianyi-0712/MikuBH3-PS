from dataclasses import dataclass
from game_server.resource.base_resource import BaseResource
from game_server.resource.decorators import GameResource

@dataclass
@GameResource("resources/ExcelOutputAsset/AvatarData.json")
class AvatarData(BaseResource):
    avatarID: int
    DefaultDressId: int
    unlockStar: int
    initialWeapon: int
    skillList: list

    def on_load(self) -> bool:
       return self.avatarID != 316 and (self.avatarID < 9000 or self.avatarID > 20000)

    def get_index(self) -> str:
        return str(self.avatarID)
