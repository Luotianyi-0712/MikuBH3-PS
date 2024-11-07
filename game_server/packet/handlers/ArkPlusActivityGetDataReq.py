
import betterproto
from game_server.net.session import Session
from lib.proto import ArkPlusActivityGetDataReq,ArkPlusActivityGetDataRsp

async def handle(session: Session, msg: ArkPlusActivityGetDataReq) -> betterproto.Message:
    return ArkPlusActivityGetDataRsp(retcode=0)
