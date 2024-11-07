import betterproto
from game_server.net.session import Session
from game_server.resource import ResourceManager
from game_server.resource.configdb.custom_head_data import CustomHeadData
from lib.proto import (
    GetCustomHeadDataReq,
    GetCustomHeadDataRsp,
    CustomHead
)

async def handle(session: Session, msg: GetCustomHeadDataReq) -> betterproto.Message:
    custom_head : CustomHead = [
        CustomHead(
            id=custom.headID
        )
        for custom in ResourceManager.instance().values(CustomHeadData)
    ]

    for i in range(161087,161091):
        custom_head.append(
            CustomHead(
                id=i
            )
        )

    for i in range(162199,162213):
        custom_head.append(
            CustomHead(
                id=i
            )
        )

    return GetCustomHeadDataRsp(
        retcode=0,
        custom_head_list=custom_head
    )
