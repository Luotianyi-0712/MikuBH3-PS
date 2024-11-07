import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetActivityRewardStatisticDataReq,
    GetActivityRewardStatisticDataRsp,
    ActivityRewardStatisticData,
    ActivityRewardStatisticItemData
)

async def handle(session: Session, msg: GetActivityRewardStatisticDataReq) -> betterproto.Message:
    return GetActivityRewardStatisticDataRsp(
        retcode=0,
        activity_reward_data=ActivityRewardStatisticData(
            id=117,
            item_data_list=[
                ActivityRewardStatisticItemData(
                    show_id=i
                )
                for i in range (506,509)
            ]
        ),
        id=117
    )
