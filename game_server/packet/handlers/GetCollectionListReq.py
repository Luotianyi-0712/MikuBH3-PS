import betterproto
from game_server.net.session import Session
from game_server.resource import ResourceManager
from game_server.resource.configdb.collection import CollectionData
from lib.proto import GetCollectionListReq, GetCollectionListRsp

async def handle(session: Session, msg: GetCollectionListReq) -> betterproto.Message:
    collection = [
        collection.ID
        for collection in ResourceManager.instance().values(CollectionData)
    ]
    return GetCollectionListRsp(
        retcode=0,
        collection_id_list=collection,
        active_collection_id_list=collection
    )
