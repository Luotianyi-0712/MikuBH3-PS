
import betterproto
from game_server.net.session import Session
from game_server.game.avatar.avatar_manager import AvatarTeamManager
from game_server.game.enum.data_type import DataType
from database import mongo
from lib.proto import (
    DelCustomAvatarTeamReq,
    DelCustomAvatarTeamRsp,
    GetAvatarTeamDataRsp,
    CustomAvatarTeam
)

async def handle(session: Session, msg: DelCustomAvatarTeamReq) -> betterproto.Message:

    session.player.custom_avatar_team_list[msg.team_id] = AvatarTeamManager(
        team_id=msg.team_id,
        name=f"Team {msg.team_id}",
        avatar_id_list=[],
        elf_id_list=[],
        astral_mate_id=0,
        is_using_astra_mate=False
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

    return DelCustomAvatarTeamRsp(retcode=0)
