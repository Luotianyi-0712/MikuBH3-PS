import betterproto
from game_server.net.session import Session
from lib.proto import GetPlayerCardReq,GetPlayerCardRsp,PlayerCardType,Medal

async def handle(session: Session, msg: GetPlayerCardReq) -> betterproto.Message:
    return GetPlayerCardRsp(
        retcode=0,
        type=PlayerCardType.CARD_ALL.value,
        elf_id_list=[0],
        avatar_id_list=[0,0,0],
        medal_list=[
            Medal(
                id=0,
                end_time=0,
                extra_param=0
            ) for i in range(2)
        ]
    )
