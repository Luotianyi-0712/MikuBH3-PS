import betterproto
from game_server.net.session import Session
from database import mongo
from lib.proto import SetClientDataReq,SetClientDataRsp

async def handle(session: Session, msg: SetClientDataReq) -> betterproto.Message:
    client_data = list(mongo.find_documents_by_key_values("clientdata", {"ID": msg.client_data.id, "Type":msg.client_data.type}))
    if not client_data:
        mongo.insert_document("clientdata",{
            "ID":msg.client_data.id,
            "Type":msg.client_data.type,
            "Data":msg.client_data.data
        })
    return SetClientDataRsp(
        retcode=0,
        id=msg.client_data.id,
        type=msg.client_data.type
    )
