from game_server.game.enum.data_type import DataType
from game_server.game.chat.decorators import Command
from game_server.net.session import Session
from database import mongo
from lib.proto import GetAvatarDataReq

@Command(
    prefix="rank",
    usage="/rank {avatar_id | all} {rank} - Edit the rank of a specific avatar or use 'all' to update the rank of all avatars.",
)
async def execute(session: Session, avatar_id, rank="1"):
    desc = getattr(execute, "usage", "No description available.")

    if not rank.isdigit():
        return f"Usage: {desc}"
    
    if avatar_id == "all":
        for avatar in session.player.avatars.values():
            await update_avatar_rank(avatar, rank, session)
        return f"Updated rank for all avatars to {rank}."

    if not avatar_id.isdigit():
        return f"Usage: {desc}"

    avatar_id = int(avatar_id)

    avatar = session.player.avatars.get(avatar_id)
    if not avatar:
        return f"Avatar with ID {avatar_id} does not exist."

    await update_avatar_rank(avatar, rank, session)

    return f"Updated avatar {avatar_id}'s rank to {rank}."

async def update_avatar_rank(avatar, rank, session:Session):
    rank = int(rank)
    if rank < 1:
        rank = 1
    if rank > 5:
        rank = 5

    avatar.star = rank

    mongo.save(session, DataType.AVATAR, [avatar.avatar_id])

    await session.process_packet(session.create_packet(GetAvatarDataReq(avatar_id_list=[avatar.avatar_id])))
