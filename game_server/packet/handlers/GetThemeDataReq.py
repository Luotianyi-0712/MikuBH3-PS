import betterproto
from game_server.net.session import Session
from game_server.resource import ResourceManager
from game_server.resource.configdb.theme_data_avatar import ThemeDataAvatar
from lib.proto import (
    GetThemeDataReq,
    GetThemeDataRsp,
    ThemeData
)

async def handle(session: Session, msg: GetThemeDataReq) -> betterproto.Message:
    return GetThemeDataRsp(
        retcode=0,
        theme_list=[
            ThemeData(
                begin_time=1583373600,
                end_time=2080843200,
                theme_id=theme.AvatarData
            )
            for theme in ResourceManager.instance().values(ThemeDataAvatar)
        ]
    )
