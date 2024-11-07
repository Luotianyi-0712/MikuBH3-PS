import betterproto
from game_server.net.session import Session
from lib.proto import GrandKeyActivateSkillReq,GrandKeyActivateSkillRsp

async def handle(session: Session, msg: GrandKeyActivateSkillReq) -> betterproto.Message:
    return GrandKeyActivateSkillRsp(retcode=0)
