import dataclasses
from database import mongo
from game_server.game.avatar.avatar_manager import AvatarManager,Skill,AvatarSubSkill,AvatarTeamManager
from game_server.game.inventory.inventory_manager import InventoryManager,Material,Weapon,Stigmata,RuneList,RuneGroup
from game_server.game.elf.elf_manager import ElfManager,ElfSkill
from game_server.game.enum.item_type import MainType

@dataclasses.dataclass
class WarshipAvatar:
    warship_first_avatar_id: int
    warship_second_avatar_id: int

@dataclasses.dataclass
class Player:
    uid: int
    name: str
    level: int
    exp: int
    hcoin: int
    stamina: int
    signature: str
    head_photo: int
    head_frame: int
    warship_id: int
    assistant_avatar_id: int
    birth_date: int
    warship_avatar: WarshipAvatar

    # Player managers
    avatars: dict[int, AvatarManager] = dataclasses.field(default_factory=dict)
    inventory: InventoryManager = dataclasses.field(default_factory=InventoryManager)
    elfs: dict[int,ElfManager] = dataclasses.field(default_factory=dict)
    custom_avatar_team_list: dict[int,AvatarTeamManager] = dataclasses.field(default_factory=dict)


    def init_default(self):
        self.add_all_avatar()
        self.add_all_items()
        self.add_all_elfs()

    def add_all_avatar(self):
        avatars = mongo.find_documents("avatars")
        for avatar in avatars:
            data = AvatarManager(
                avatar_id=avatar['AvatarID'],
                star=avatar['Star'],
                level=avatar['Level'],
                exp=avatar['Exp'],
                fragment=avatar['Fragment'],
                touch_good_feel=avatar['TouchGoodFeel'],
                today_has_add_good_feel=avatar['TodayHasAddGoodFeel'],
                dress_id=avatar['DressID'],
                dress_lists=avatar['DressLists'],
                sub_star=avatar['SubStar'],
                skill_lists={
                    skill['SkillId']:
                    Skill(
                        skill_id=skill['SkillId'],
                        sub_skill_lists={
                            sub_skill['subSkillId']:
                                AvatarSubSkill(
                                    sub_skill_id=sub_skill['subSkillId'],
                                    level=sub_skill['level']
                                )
                                for sub_id,sub_skill in skill['SubSkillLists'].items()
                        }
                    )
                    for id,skill in avatar['SkillLists'].items()
                }
            )
            weapon = list(mongo.find_documents_by_key_values("items", {"EquipAvatarID": avatar['AvatarID'], "MainType":MainType.WEAPON.value}))
            stigmata = list(mongo.find_documents_by_key_values("items", {"EquipAvatarID": avatar['AvatarID'], "MainType":MainType.STIGMATA.value}))
            if any(weapon):
                data.weapon_id = weapon[0]['UniqueID']
            if any(stigmata):
                for stigma in stigmata:
                    data.stigmata_ids[stigma['SlotNum']] = stigma['UniqueID']
            self.avatars[avatar['AvatarID']] = data

    def add_all_items(self):
        get_items = mongo.find_documents("items")
        for item in get_items:
            if item['MainType'] == MainType.MATERIAL.value:
                normal_item = Material(
                    item_id=item['ItemID'],
                    num=item['ItemNum']
                )
                self.inventory.material_items[item['ItemID']] = normal_item

            if item['MainType'] == MainType.WEAPON.value:
                weapon = Weapon(
                    item_id=item['ItemID'],
                    level=item['Level'],
                    exp=item['Exp'],
                    is_locked=item['IsLocked'],
                    is_extracted=item['IsExtracted'],
                    equip_avatar_id=item['EquipAvatarID']
                )
                self.inventory.weapon_items[item['UniqueID']] = weapon
            
            if item['MainType'] == MainType.STIGMATA.value:
                stigmata = Stigmata(
                    item_id=item['ItemID'],
                    level=item['Level'],
                    exp=item['Exp'],
                    slot_num=item['SlotNum'],
                    refine_value=item['RefineValue'],
                    promote_times=item['PromoteTimes'],
                    is_locked=item['IsLocked'],
                    equip_avatar_id=item['EquipAvatarID'],
                    rune_list=[
                        RuneList(
                            rune_id=rune['RuneId'],
                            strength_percent=rune['strengthPercent']
                        )
                        for rune in item['RuneLists']
                    ]
                )
                self.inventory.stigmata_items[item['UniqueID']] = stigmata

    def add_all_elfs(self):
        get_elfs = mongo.find_documents("elfs")
        for elf in get_elfs:
            data = ElfManager(
                elf_id=elf['ElfId'],
                level=elf['Level'],
                star=elf['Star'],
                exp=elf['Exp'],
                skill_list={
                    skill['SkillId']:
                        ElfSkill(
                            skill_id=skill['SkillId'],
                            level=skill['Level']
                        )
                    for id,skill in elf['SkillLists'].items()
                }
            )
            self.elfs[elf['ElfId']] = data