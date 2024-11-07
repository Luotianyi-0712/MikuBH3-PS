import betterproto
from game_server.net.session import Session
from lib.proto import (
    GetAvatarTeamDataReq,
    GetAvatarTeamDataRsp,
    CustomAvatarTeam
)

async def handle(session: Session, msg: GetAvatarTeamDataReq) -> betterproto.Message:
    return GetAvatarTeamDataRsp(
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
    )
