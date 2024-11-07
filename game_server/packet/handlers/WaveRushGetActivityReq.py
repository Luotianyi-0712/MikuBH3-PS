import betterproto
from game_server.net.session import Session
from lib.proto import WaveRushGetActivityReq, WaveRushGetActivityRsp

async def handle(session: Session, msg: WaveRushGetActivityReq) -> betterproto.Message:
    return WaveRushGetActivityRsp(retcode=0)
