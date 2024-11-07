import betterproto
from game_server.net.session import Session
from lib.proto import GetAdventureGroupReq, GetAdventureGroupRsp

async def handle(session: Session, msg: GetAdventureGroupReq) -> betterproto.Message:
    return GetAdventureGroupRsp(retcode=0)
