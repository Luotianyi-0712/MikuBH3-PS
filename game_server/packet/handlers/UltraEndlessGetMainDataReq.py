import betterproto
import json
from game_server.net.session import Session
from lib.proto import (
    UltraEndlessGetMainDataReq,
    UltraEndlessGetMainDataRsp,
    UltraEndlessMainData,
    UltraEndlessPlayer,
    UltraEndlessSettleInfo,
    UltraEndlessFloor,
    UltraEndlessSite,
    PlayerFriendBriefData
)

async def handle(session: Session, msg: UltraEndlessGetMainDataReq) -> betterproto.Message:
    with open("Battle.json", "r") as file:
        data = json.load(file)

    endless_data = data.get("endless", {})
    site = endless_data.get("area1", 781009)
    group = endless_data.get("grouplevel", 9)
    dynamic = endless_data.get("dynamic", 500)
    cupnum = endless_data.get("cupnum", 1600)
    return UltraEndlessGetMainDataRsp(
        retcode=0,
        dynamic_hard_level=dynamic,
        cup_num=cupnum,
        endless_player_list=[
            UltraEndlessPlayer(
                cup_num=cupnum,
                group_level=group,
                uid=1337
            )
        ],
        group_level=group,
        last_settle_info=UltraEndlessSettleInfo(
            cup_num=cupnum,
            cup_num_after_schedule_settle=cupnum,
            cup_num_after_season_settle=975,
            cup_num_before=cupnum,
            cup_num_before_season_settle=975,
            group_level=group,
            group_member_num=20,
            max_stage_score=21792,
            mmr_score=1618,
            rank=9,
            schedule_id=3365
        ),
        main_data=UltraEndlessMainData(
            begin_time=1730098800,
            close_time=1880308800,
            cur_season_id=119,
            effect_time=1880308800,
            end_time=1880308800,
            last_schedule_id=3366,
            last_settle_top_rank_schedule_id=3366,
            schedule_id=3366,
            site_list=[
                UltraEndlessSite(
                    floor_list=[
                        UltraEndlessFloor(
                            floor=1,
                            max_score=1000
                        ),
                        UltraEndlessFloor(
                            floor=2,
                            max_score=1000
                        ),
                        UltraEndlessFloor(
                            floor=3,
                            max_score=1000
                        ),
                        UltraEndlessFloor(
                            floor=4,
                            max_score=1000
                        ),
                        UltraEndlessFloor(
                            floor=5,
                            max_score=2000
                        )
                    ],
                    max_score_cost_time=87,
                    site_id=site
                ),
                UltraEndlessSite(
                    floor_list=[
                        UltraEndlessFloor(
                            floor=1,
                            max_score=1000
                        ),
                        UltraEndlessFloor(
                            floor=2,
                            max_score=1000
                        ),
                        UltraEndlessFloor(
                            floor=3,
                            max_score=1000
                        ),
                        UltraEndlessFloor(
                            floor=4,
                            max_score=1000
                        ),
                        UltraEndlessFloor(
                            floor=5,
                            max_score=2000
                        )
                    ],
                    max_score_cost_time=119,
                    site_id=site+1
                ),
                UltraEndlessSite(
                    floor_list=[
                        UltraEndlessFloor(
                            floor=1,
                            max_score=1000
                        ),
                        UltraEndlessFloor(
                            floor=2,
                            max_score=2826
                        )
                    ],
                    max_score_cost_time=52,
                    site_id=site+2
                ),
                UltraEndlessSite(
                    floor_list=[
                        UltraEndlessFloor(
                            floor=1,
                            max_score=1000
                        ),
                        UltraEndlessFloor(
                            floor=2,
                            max_score=1000
                        ),
                        UltraEndlessFloor(
                            floor=3,
                            max_score=1000
                        ),
                        UltraEndlessFloor(
                            floor=4,
                            max_score=1000
                        ),
                        UltraEndlessFloor(
                            floor=5,
                            max_score=2000
                        )
                    ],
                    max_score_cost_time=113,
                    site_id=site+3
                )
            ]
        ),
        schedule_id=3366,
        top_group_level=9,
        brief_data_list=[
            PlayerFriendBriefData(
                uid=1337,
                nickname="Miku",
                avatar_id=3101,
                avatar_level=80,
                avatar_star=3,
                comfort_value=217,
                custom_head_id=161099,
                dress_id=50217,
                frame_id=200080,
                house_level=1,
                is_allow_visit=True,
                last_login_time=1730263760,
                last_logout_time=1730264009,
                level=88,
                online_status=3,
                show_house=101,
                visit_avatar=101
            )
        ]
    )
