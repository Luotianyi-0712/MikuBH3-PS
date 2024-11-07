import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetPhonePendantDataReq,
    GetPhonePendantDataRsp,
    PhonePendant
)

async def handle(session: Session, msg: GetPhonePendantDataReq) -> betterproto.Message:
    phone = [350005,350011,350012,350013,350014,350015,350026,350041,350044,350045,350049,350051,350053,350054,350061,350305]
    return GetPhonePendantDataRsp(
        retcode=0,
        is_all=True,
        phone_pendant_list=[
            PhonePendant(
                id=id
            )
            for id in phone
        ]
    )
