from database import mongo
from lib.proto import GetAvatarDataReq, AvatarSubSkill
from game_server.net.session import Session
from game_server.resource import ResourceManager
from game_server.game.enum.data_type import DataType
from game_server.game.chat.decorators import Command
from game_server.resource.configdb.avatar_sub_skill_data import AvatarSubSkillData

@Command(
    prefix="maxskill",
    usage="/maxskill {avatar_id | all} - Maximize the skills of a specific avatar. Use 'all' to maximize the skills of all avatars.",
)
async def execute(session: Session, avatar_id):
    desc = getattr(execute, "usage", "No description available.")

    if avatar_id == "all":
        for avatar in session.player.avatars.values():
            await max_out_skills_for_avatar(avatar, session)
        return "All avatars' skills have been maxed out!"

    if not avatar_id.isdigit():
        return f"Usage: {desc}"

    avatar_id = int(avatar_id)

    avatar = session.player.avatars.get(avatar_id)
    if not avatar:
        return f"Avatar with ID {avatar_id} does not exist."

    await max_out_skills_for_avatar(avatar, session)

    return f"All skills for avatar {avatar_id} have been maxed out!"

async def max_out_skills_for_avatar(avatar, session:Session):
    resource_manager = ResourceManager.instance()
    for skill_id, skill in avatar.skill_lists.items():
        sub_skills = [
            data for data in resource_manager.values(AvatarSubSkillData) 
            if data.skillId == skill_id
        ]
        for sub_skill_data in sub_skills:
            skill.sub_skill_lists[sub_skill_data.avatarSubSkillId] = AvatarSubSkill(
                sub_skill_id=sub_skill_data.avatarSubSkillId,
                level=sub_skill_data.maxLv
            )

    mongo.save(session, DataType.AVATAR, [avatar.avatar_id])
    await session.process_packet(session.create_packet(GetAvatarDataReq(avatar_id_list=[avatar.avatar_id])))
