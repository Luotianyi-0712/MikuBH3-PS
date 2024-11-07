import betterproto
import traceback
from database import mongo
from game_server.net.session import Session
from game_server.game.player import Player,WarshipAvatar
from game_server.game.avatar.avatar_manager import AvatarTeamManager
from lib.proto import (
    PlayerLoginReq,
    PlayerLoginRsp,
    GetMpDataRsp,
    MpDataType,
    CGType,
    GetMpDataRspOpType
)
    
async def handle(session: Session, msg: PlayerLoginReq) -> betterproto.Message:
    try:
        data = mongo.find_documents("players")[0]
        session.player = Player(
            uid=data['UID'],
            name=data['Name'],
            level=data['Level'],
            exp=data['Exp'],
            hcoin=data['HCoin'],
            stamina=data['Stamina'],
            signature=data['Sign'],
            head_photo=data['HeadPhoto'],
            head_frame=data['HeadFrame'],
            warship_id=data['WarshipId'],
            assistant_avatar_id=data['AssistantAvatarId'],
            birth_date=data['BirthDate'],
            warship_avatar=WarshipAvatar(
                warship_first_avatar_id=data['WarshipAvatar']['WarshipFirstAvatarId'],
                warship_second_avatar_id=data['WarshipAvatar']['WarshipSecondAvatarId']
            )
        )

        for team_id,team in data['CustomAvatarTeamList'].items():
            session.player.custom_avatar_team_list[int(team_id)] = AvatarTeamManager(
                team_id=int(team_id),
                name=team['Name'],
                astral_mate_id=team['astraMateId'],
                is_using_astra_mate=team['isUsingAstraMate'],
                elf_id_list=team['elfIdList'],
                avatar_id_list=team['AvatarIdLists']
            )


        session.player.init_default()
        session.pending_notify(GetMpDataRsp(
            retcode=0,
            data_type=MpDataType.MP_DATA_PUNISH_TIME.value,
            op_type=GetMpDataRspOpType.UPDATE_DATA.value,
            punish_end_time=0
        ))
        return PlayerLoginRsp(
            retcode=0,
            is_first_login=False,
            region_name="overseas01",
            cg_type=CGType.CG_SEVEN_CHAPTER.value,
            region_id=248,
            login_session_token=1,
            psycho_key=0
        )
    except:
        traceback.print_exc()
        return
