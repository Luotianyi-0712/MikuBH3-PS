import betterproto
from game_server.net.session import Session
from database import mongo
from lib.proto import GetClientDataReq,GetClientDataRsp,ClientData

async def handle(session: Session, msg: GetClientDataReq) -> betterproto.Message:
    data = []
    client_data = list(mongo.find_documents_by_key_values("clientdata", {"ID": msg.id, "Type":msg.type}))
    if client_data:
        for client in client_data:
            data.append(
                ClientData(
                    id=client['ID'],
                    type=client['Type'],
                    data=client['Data'][0]
                )
            )
    return GetClientDataRsp(
        retcode=0,
        type=msg.type,
        id=msg.id,
        client_data_list=data
    )
