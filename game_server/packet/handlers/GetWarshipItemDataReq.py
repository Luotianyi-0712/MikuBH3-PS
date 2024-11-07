import betterproto
from game_server.net.session import Session
from game_server.resource import ResourceManager
from game_server.resource.configdb.entry_theme_item_data import EntryThemeItemData
from lib.proto import GetWarshipItemDataReq, GetWarshipItemDataRsp

async def handle(session: Session, msg: GetWarshipItemDataReq) -> betterproto.Message:
    return GetWarshipItemDataRsp(
        retcode=0,
        is_all=True,
        warship_item_id_list=[
            theme.ThemeItemID
            for theme in ResourceManager.instance().values(EntryThemeItemData)
        ]
    )
