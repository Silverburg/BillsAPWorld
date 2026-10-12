from __future__ import annotations

from typing import TYPE_CHECKING
from .constants import GAME_NAME, CLASSIFICATION
from .data.data_items import *

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import BillsAPWorld

class BillsAPItem(Item):
    game = GAME_NAME

def get_random_filler_item_name(world: BillsAPWorld) -> str:

    if world.random.randint(0, 99) < world.options.trap_chance:
        return TRAP
    return FILLER

def create_all_items(world: BillsAPWorld) -> None:
    itempool = [world.create_item(item) for item, values in ITEM_LIST.items() if values[CLASSIFICATION] not in(ItemClassification.filler, ItemClassification.trap)]

    needed_filler = len(world.multiworld.get_unfilled_locations(world.player)) - len(itempool)
    itempool += [world.create_filler() for _ in range(needed_filler)]

    world.multiworld.itempool += itempool

