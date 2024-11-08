import betterproto
from game_server.net.session import Session
from game_server.resource import ResourceManager
from game_server.resource.configdb.frame_data import Frame_Data
from utils.time import get_unix_in_seconds
from lib.proto import GetFrameDataReq, GetFrameDataRsp, FrameData


async def handle(session: Session, msg: GetFrameDataReq) -> betterproto.Message:
    return GetFrameDataRsp(
        retcode=0,
        is_all=True,
        frame_list=[
            FrameData(id=frame.id, expire_time=get_unix_in_seconds() + 3600 * 24 * 7)
            for frame in ResourceManager.instance().values(Frame_Data)
        ],
    )
