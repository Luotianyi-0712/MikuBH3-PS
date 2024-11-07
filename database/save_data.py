from game_server.game.enum.data_type import DataType

class SaveData:
    def __init__(self, mongo, session, data_type:DataType, ids: list):
        self.mongo = mongo
        self.session = session
        self.data_type = data_type
        self.ids = ids

    def save(self):
        data_type_handlers = {
            DataType.MATERIAL: self._save_material,
            DataType.WEAPON: self._save_weapon,
            DataType.STIGMATA: self._save_stigmata,
            DataType.AVATAR: self._save_avatar,
            DataType.PLAYER: self._save_player
        }
        handler = data_type_handlers.get(self.data_type)
        if handler:
            handler()
        else:
            raise ValueError(f"Unsupported data type: {self.data_type}")

    def _save_material(self):
        for id in self.ids:
            get_item = self.session.player.inventory.material_items.get(id)
            if get_item:
                filter = {"ItemID": get_item.item_id}
                update = {"$set": {"Num": get_item.num}}
                self.mongo.update_document("items",filter,update)

    def _save_weapon(self):
        for unique_id in self.ids:
            if id == 0:
                continue
            get_item = self.session.player.inventory.weapon_items.get(unique_id)
            if get_item:
                filter = {"UniqueID": unique_id}
                update = {
                            "$set": 
                            {
                                "Level": get_item.level,
                                "Exp": get_item.exp,
                                "IsLocked" : get_item.is_locked,
                                "IsExtracted" : get_item.is_extracted,
                                "EquipAvatarID" : get_item.equip_avatar_id
                            }
                        }
                self.mongo.update_document("items",filter,update)
    def _save_stigmata(self):
        for unique_id in self.ids:
            if id == 0:
                continue
            get_item = self.session.player.inventory.stigmata_items.get(unique_id)
            if get_item:
                filter = {"UniqueID": unique_id}
                update = {
                            "$set": 
                            {
                                "Level": get_item.level,
                                "Exp": get_item.exp,
                                "SlotNum": get_item.slot_num,
                                "IsLocked" : get_item.is_locked,
                                "EquipAvatarID" : get_item.equip_avatar_id
                            }
                        }
                self.mongo.update_document("items",filter,update)


    def _save_avatar(self):
        for id in self.ids:
            avatar = self.session.player.avatars.get(id)
            if avatar:
                filter = {"AvatarID": id}
                update = {
                            "$set": 
                            {
                                "Star": avatar.star,
                                "Fragment": avatar.fragment,
                                "TouchGoodFeel" : avatar.touch_good_feel,
                                "TodayHasAddGoodFeel" : avatar.today_has_add_good_feel,
                                "DressID" : avatar.dress_id,
                                "SkillLists" : {
                                    f"{skill_id}":{
                                        "SkillId":skill.skill_id,
                                        "SubSkillLists":{
                                            f"{sub_skill.sub_skill_id}":{
                                                "subSkillId":sub_skill.sub_skill_id,
                                                "level":sub_skill.level
                                            }
                                            for sub_id, sub_skill in skill.sub_skill_lists.items()
                                        }
                                    }
                                    for skill_id,skill in avatar.skill_lists.items()
                                },
                            }
                        }
                self.mongo.update_document("avatars",filter,update)

    def _save_player(self):
        filter = {"UID": self.session.player.uid}
        update = {
            "$set":
            {
                "Name": self.session.player.name,
                "HCoin": self.session.player.hcoin,
                "Sign": self.session.player.signature,
                "HeadPhoto": self.session.player.head_photo,
                "HeadFrame": self.session.player.head_frame,
                "WarshipId": self.session.player.warship_id,
                "AssistantAvatarId": self.session.player.assistant_avatar_id,
                "WarshipAvatar":{
                    "WarshipFirstAvatarId": self.session.player.warship_avatar.warship_first_avatar_id,
                    "WarshipSecondAvatarId": self.session.player.warship_avatar.warship_second_avatar_id
                },
                "BirthDate":self.session.player.birth_date,
                "CustomAvatarTeamList":{
                    f"{team_id}":{
                        "TeamId":team_id,
                        "Name": team.name,
                        "astraMateId":team.astral_mate_id,
                        "isUsingAstraMate":team.is_using_astra_mate,
                        "elfIdList":team.elf_id_list,
                        "AvatarIdLists":team.avatar_id_list
                    }
                    for team_id,team in self.session.player.custom_avatar_team_list.items()
                }
            }
        }
        self.mongo.update_document("players",filter,update)