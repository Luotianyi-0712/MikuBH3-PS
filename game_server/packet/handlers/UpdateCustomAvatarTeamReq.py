import betterproto
from game_server.net.session import Session
from game_server.game.avatar.avatar_manager import AvatarTeamManager
from game_server.game.enum.data_type import DataType
from database import mongo
from lib.proto import (
    UpdateCustomAvatarTeamReq,
    UpdateCustomAvatarTeamRsp,
    GetAvatarTeamDataRsp,
    CustomAvatarTeam
)

async def handle(session: Session, msg: UpdateCustomAvatarTeamReq) -> betterproto.Message:

    team = msg.team

    session.player.custom_avatar_team_list[team.team_id] = AvatarTeamManager(
        team_id=team.team_id,
        name=team.name,
        avatar_id_list=team.avatar_id_list,
        elf_id_list=team.elf_id_list,
        astral_mate_id=team.astra_mate_id,
        is_using_astra_mate=team.is_using_astra_mate
    )

    await session.send(session.create_packet(GetAvatarTeamDataRsp(
        retcode=0,
        custom_avatar_team_list=[
            CustomAvatarTeam(
                team_id=team.team_id,
                name=team.name,
                avatar_id_list=team.avatar_id_list,
                elf_id_list=team.elf_id_list,
                astra_mate_id=team.astral_mate_id,
                is_using_astra_mate=team.is_using_astra_mate
            )
            for team_id,team in session.player.custom_avatar_team_list.items()
        ]
    )))

    mongo.save(session,DataType.PLAYER)

    return UpdateCustomAvatarTeamRsp(retcode=0)
