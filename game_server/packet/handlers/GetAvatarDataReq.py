import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetAvatarDataReq,
    GetAvatarDataRsp,
    Avatar,
    AvatarSkill,
    AvatarSubSkill
)

async def handle(session: Session, msg: GetAvatarDataReq) -> betterproto.Message:
    rsp = GetAvatarDataRsp(retcode=0)
    if len(msg.avatar_id_list) == 1 and int(msg.avatar_id_list[0]) == 0 :
        rsp.is_all = True
        rsp.avatar_list=[
            Avatar(
                avatar_id=avatar.avatar_id,
                star=avatar.star,
                level=avatar.level,
                exp=avatar.exp,
                fragment=avatar.fragment,
                weapon_unique_id=avatar.weapon_id,
                stigmata_unique_id_1=avatar.stigmata_ids.get(1,0),
                stigmata_unique_id_2=avatar.stigmata_ids.get(2,0),
                stigmata_unique_id_3=avatar.stigmata_ids.get(3,0),
                skill_list=[
                    AvatarSkill(
                        skill_id=skill_id,
                        sub_skill_list=[
                            AvatarSubSkill(
                                sub_skill_id=sub_skill.sub_skill_id,
                                level=sub_skill.level
                            )
                            for sub_id, sub_skill in skill.sub_skill_lists.items()
                        ]
                    )
                    for skill_id,skill in avatar.skill_lists.items()
                ],
                touch_goodfeel=avatar.touch_good_feel,
                today_has_add_goodfeel=avatar.today_has_add_good_feel,
                dress_list=avatar.dress_lists,
                dress_id=avatar.dress_id,
                sub_star=avatar.sub_star
            )
            for id, avatar in session.player.avatars.items()
        ]
    else:
        avatar_list = []
        for id in msg.avatar_id_list:
            avatar = session.player.avatars.get(id)
            avatar_list.append(
                Avatar(
                    avatar_id=avatar.avatar_id,
                    star=avatar.star,
                    level=avatar.level,
                    exp=avatar.exp,
                    fragment=avatar.fragment,
                    weapon_unique_id=avatar.weapon_id,
                    stigmata_unique_id_1=avatar.stigmata_ids.get(1,0),
                    stigmata_unique_id_2=avatar.stigmata_ids.get(2,0),
                    stigmata_unique_id_3=avatar.stigmata_ids.get(3,0),
                    skill_list=[
                        AvatarSkill(
                            skill_id=skill_id,
                            sub_skill_list=[
                                AvatarSubSkill(
                                    sub_skill_id=sub_skill.sub_skill_id,
                                    level=sub_skill.level
                                )
                                for sub_id, sub_skill in skill.sub_skill_lists.items()
                            ]
                        )
                        for skill_id,skill in avatar.skill_lists.items()
                    ],
                    touch_goodfeel=avatar.touch_good_feel,
                    today_has_add_goodfeel=avatar.today_has_add_good_feel,
                    dress_list=avatar.dress_lists,
                    dress_id=avatar.dress_id,
                    sub_star=avatar.sub_star
                )
            )
        rsp.is_all = False
        rsp.avatar_list=avatar_list
    return rsp