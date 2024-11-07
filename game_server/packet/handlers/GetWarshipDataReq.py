import betterproto
from game_server.net.session import Session
from game_server.resource import ResourceManager
from game_server.resource.configdb.entry_theme_data import EntryThemeData
from lib.proto import (
    GetWarshipDataReq,
    GetWarshipDataRsp,
    WarshipThemeData,
    WarshipComponent
)

async def handle(session: Session, msg: GetWarshipDataReq) -> betterproto.Message:

    warship = []
    for theme in ResourceManager.instance().values(EntryThemeData):
        ship = WarshipThemeData(
            warship_id=theme.SpaceShipConfigID,
            bgm_play_mode=1,
            is_weather_fixed=True
        )

        if theme.ThemeBGMConfigList:
            ship.component_list = WarshipComponent(
                component_id=theme.ThemeBGMConfigList[0],
                type=2
            )
        if theme.ThemeTagList:
            ship.weather_idx = theme.ThemeTagList[0]
        warship.append(ship)

    return GetWarshipDataRsp(
        retcode=0,
        is_all=True,
        warship_list=warship
    )
