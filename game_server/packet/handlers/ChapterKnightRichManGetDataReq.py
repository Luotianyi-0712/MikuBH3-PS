import betterproto
from game_server.net.session import Session
from lib.proto import ChapterKnightRichManGetDataReq, ChapterKnightRichManGetDataRsp

async def handle(session: Session, msg: ChapterKnightRichManGetDataReq) -> betterproto.Message:
    return ChapterKnightRichManGetDataRsp(retcode=0,rich_man_id=101)
