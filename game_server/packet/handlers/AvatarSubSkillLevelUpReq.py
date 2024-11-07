import betterproto
from game_server.net.session import Session
from game_server.game.enum.data_type import DataType
from game_server.resource import ResourceManager
from game_server.resource.configdb.avatar_sub_skill_data import AvatarSubSkillData
from database import mongo
from lib.proto import (
    AvatarSubSkillLevelUpReq,
    AvatarSubSkillLevelUpRsp,
    AvatarSubSkill,
    GetAvatarDataReq,
    GetEquipmentDataRsp,
    Material
)

async def handle(session: Session, msg: AvatarSubSkillLevelUpReq) -> betterproto.Message:
    avatar_data = session.player.avatars.get(msg.avatar_id)
    if not avatar_data:
        return AvatarSubSkillLevelUpRsp(retcode=2)

    skill_data = avatar_data.skill_lists.get(msg.skill_id)
    if not skill_data:
        return AvatarSubSkillLevelUpRsp(retcode=3)

    sub_skill_data = ResourceManager.instance().find_by_index(AvatarSubSkillData, msg.sub_skill_id)
    if not sub_skill_data:
        return AvatarSubSkillLevelUpRsp(retcode=4)

    sub_skill = skill_data.sub_skill_lists.get(msg.sub_skill_id)
    if not sub_skill:
        skill_data.sub_skill_lists[msg.sub_skill_id] = AvatarSubSkill(
            sub_skill_id=msg.sub_skill_id,
            level=0
        )

    current_level = skill_data.sub_skill_lists[msg.sub_skill_id].level
    new_level = sub_skill_data.maxLv if msg.is_level_up_all else current_level + 1

    if new_level > sub_skill_data.maxLv:
        return AvatarSubSkillLevelUpRsp(retcode=10)

    skill_data.sub_skill_lists[msg.sub_skill_id] = AvatarSubSkill(
        sub_skill_id=msg.sub_skill_id,
        level=new_level
    )
    avatar_data.skill_lists[msg.skill_id] = skill_data

    await session.process_packet(session.create_packet(GetAvatarDataReq(avatar_id_list=[msg.avatar_id])))

    coin = session.player.inventory.material_items.get(100)
    if coin:
        session.pending_notify(
            GetEquipmentDataRsp(
                material_list=[Material(id=coin.item_id, num=coin.num)]
            )
        )

    mongo.save(session, DataType.AVATAR, [msg.avatar_id])

    return AvatarSubSkillLevelUpRsp(retcode=0)
