import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetMasterPupilApplyReq,
    GetMasterPupilApplyRsp,
    MasterPupilType
)

async def handle(session: Session, msg: GetMasterPupilApplyReq) -> betterproto.Message:
    return GetMasterPupilApplyRsp(
        retcode=0,
        type=MasterPupilType.MASTER_PUPIL_MASTER_TYPE.value
    )
