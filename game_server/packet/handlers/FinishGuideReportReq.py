import betterproto
from game_server.net.session import Session
from lib.proto import FinishGuideReportReq,FinishGuideReportRsp

async def handle(session: Session, msg: FinishGuideReportReq) -> betterproto.Message:
    print(msg.guide_id_list)
    return FinishGuideReportRsp(
        retcode=0,
        guide_id_list=msg.guide_id_list,
        is_finish=True
    )


