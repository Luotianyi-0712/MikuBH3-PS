import time
import json
import random
from game_server.resource import ResourceManager
from game_server.resource.configdb.avatar_data import AvatarData
from game_server.resource.configdb.weapon_data import WeaponData
from game_server.resource.configdb.stigmata_data import StigmataData
from game_server.resource.configdb.material_data import MaterialData
from game_server.resource.configdb.elf_astra_mate_data import ElfAstraMateData
from game_server.resource.configdb.dress_data import DressData
from game_server.game.enum.item_type import MainType

class MongoDBCreate:
    def __init__(self, mongo):
        self.mongo = mongo
        self.manager = ResourceManager.instance()
        self.create_db()
        self.avatars()
        self.items()
        self.elfs()

    def create_db(self):
        player_data = {
            "UID": 1337,
            "Name": "Miku",
            "Level": 88,
            "Exp": 0,
            "HCoin": 1337,
            "Stamina": 80,
            "Sign": "MikuPS",
            "HeadPhoto": 161090,
            "HeadFrame": 200001,
            "WarshipId": 400004,
            "AssistantAvatarId": 101,
            "WarshipAvatar": {
                "WarshipFirstAvatarId": 101,
                "WarshipSecondAvatarId": 0
            },
            "BirthDate": 0,
            "CustomAvatarTeamList":{
                f"{i}":{
                    "TeamId":i,
                    "Name": f"Team {i}",
                    "astraMateId":0,
                    "isUsingAstraMate":False,
                    "elfIdList":[],
                    "AvatarIdLists":[]
                }
                for i in range(1,11)
            }
        }
        self.mongo.insert_document("players",player_data)

    def avatars(self):
        data = []
        for avatar in self.manager.instance().values(AvatarData):
            valk = {
                "AvatarID":avatar.avatarID,
                "Star":avatar.unlockStar,
                "Level":80,
                "Exp":0,
                "Fragment":0,
                "TouchGoodFeel":0,
                "TodayHasAddGoodFeel":0,
                "DressID":avatar.DefaultDressId,
                "DressLists":[
                    dress.dressID
                    for dress in self.manager.instance().values(DressData)
                    if avatar.avatarID in dress.avatarIDList
                ],
                "AvatarArtifact":None,
                "SubStar":0,
                "SkillLists": {
                    f"{skillId}": {
                        "SkillId": skillId,
                        "SubSkillLists": {}
                    }
                    for skillId in avatar.skillList
                },
                "CreateTime":int(time.time())
            }
            data.append(valk)
        self.mongo.get_collection("avatars").insert_many(data)

    def items(self):
        last_item = self.mongo.get_collection("items").find_one(sort=[("UniqueID", -1)])
        unique_id = last_item["UniqueID"] + 1 if last_item else 1
        
        items_data = []

        for weapon in self.manager.instance().values(WeaponData):
            if weapon.rarity == weapon.maxRarity:
                weapon_data = {
                    "UniqueID":unique_id,
                    "ItemID":weapon.ID,
                    "Level":weapon.maxLv,
                    "Exp":0,
                    "IsLocked":False,
                    "IsExtracted":False,
                    "QuantumBranchLists":None,
                    "MainType":MainType.WEAPON.value,
                    "EquipAvatarID":0
                }
                items_data.append(weapon_data)
                unique_id += 1

        for stigmata in self.manager.instance().values(StigmataData):
            if stigmata.rarity == stigmata.maxRarity:
                stigmata_data = {
                    "UniqueID":unique_id,
                    "ItemID":stigmata.ID,
                    "Level":stigmata.maxLv,
                    "Exp":0,
                    "SlotNum":0,
                    "RefineValue":0,
                    "PromoteTimes":0,
                    "IsLocked":False,
                    "RuneLists":[],
                    "WaitSelectRuneLists":[],
                    "WaitSelectRuneGroupLists":[],
                    "MainType":MainType.STIGMATA.value,
                    "EquipAvatarID":0
                }
                items_data.append(stigmata_data)
                unique_id += 1

        for material in self.manager.instance().values(MaterialData):
            material = {
                "ItemID":material.ID,
                "ItemNum":99999999 if material.ID == 100 else (999 if material.quantityLimit > 999 else material.quantityLimit),
                "MainType":MainType.MATERIAL.value,
            }
            items_data.append(material)

        for avatar in self.manager.instance().values(AvatarData):
            avatar_data = {
                "UniqueID":unique_id,
                "ItemID":avatar.initialWeapon,
                "Level":15,
                "Exp":0,
                "IsLocked":False,
                "IsExtracted":False,
                "QuantumBranchLists":None,
                "MainType":MainType.WEAPON.value,
                "EquipAvatarID":avatar.avatarID
            }
            items_data.append(avatar_data)
            unique_id += 1
        
        self.mongo.get_collection("items").insert_many(items_data)

    def elfs(self):
        elfs_data = []
        for elf in self.manager.instance().values(ElfAstraMateData):
            elf_data = {
                "ElfId":elf.ElfID,
                "Level":elf.MaxLevel,
                "Star":elf.MaxRarity,
                "Exp":0,
                "SkillLists":{
                    f"{skill.ElfSkillID}":{
                        "SkillId":skill.ElfSkillID,
                        "Level":skill.MaxLv
                    }
                    for skill in elf.skill_lists
                }
            }
            elfs_data.append(elf_data)
        self.mongo.get_collection("elfs").insert_many(elfs_data)
