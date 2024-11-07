import dataclasses

@dataclasses.dataclass
class Material:
    item_id : int
    num : int

@dataclasses.dataclass
class Weapon:
    item_id : int
    level : int
    exp : int
    is_locked : bool
    is_extracted : bool
    equip_avatar_id: int

@dataclasses.dataclass
class Stigmata:
    item_id : int
    level : int
    exp : int
    slot_num : int
    refine_value : int
    promote_times : int
    is_locked : bool
    equip_avatar_id : int

@dataclasses.dataclass
class InventoryManager:
    material_items : dict[int,Material] = dataclasses.field(default_factory=dict)
    weapon_items : dict[int,Weapon] = dataclasses.field(default_factory=dict)
    stigmata_items : dict[int,Stigmata] = dataclasses.field(default_factory=dict)