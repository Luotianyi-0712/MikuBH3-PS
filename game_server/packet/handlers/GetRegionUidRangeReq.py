import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetRegionUidRangeReq,
    GetRegionUidRangeRsp,
    RegionUidRange
)

async def handle(session: Session, msg: GetRegionUidRangeReq) -> betterproto.Message:
    return GetRegionUidRangeRsp(
        retcode=0,
        local_region_name="overseas01",
        region_uid_range_list=[
            RegionUidRange(
                end_uid=50000000,
                region_name="overseas01",
                start_uid=1000
            )
        ]
    )
