import betterproto
from game_server.net.session import Session
from game_server.resource import ResourceManager
from game_server.resource.configdb.recommend_panel import RecommendPanelData
from lib.proto import (
    GetRecommendMissionPanelListReq,
    GetRecommendMissionPanelListRsp,
    RecommendMissionPanel
)

async def handle(session: Session, msg: GetRecommendMissionPanelListReq) -> betterproto.Message:
    panel_list : RecommendMissionPanel = [
        RecommendMissionPanel(
            panel_id=panel.PanelID,
            is_panel_show=True,
            mission_begin_time=0
        )
        for panel in ResourceManager.instance().values(RecommendPanelData)
    ]

    return GetRecommendMissionPanelListRsp(
        retcode=0,
        recommend_mission_panel_list=panel_list
    )
