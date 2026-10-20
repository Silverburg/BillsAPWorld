from __future__ import annotations

from typing import TYPE_CHECKING
from .constants import GAME_NAME, CLASSIFICATION, AMOUNT
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
    itempool = []
    for item in filter(lambda item: ITEM_LIST[item][CLASSIFICATION] not in (ItemClassification.filler, ItemClassification.trap), ITEM_LIST.keys()):
        if AMOUNT in ITEM_LIST[item]:
            for i in range(ITEM_LIST[item][AMOUNT]):
                print(f"Adding item: {item}")
                itempool.append(world.create_item(item))
        else:
            print(f"Adding item: {item}")
            itempool.append(world.create_item(item))

    print(itempool)

    needed_filler = len(world.multiworld.get_unfilled_locations(world.player)) - len(itempool)
    itempool += [world.create_filler() for _ in range(needed_filler)]

    print("----")
    print(itempool)

    world.multiworld.itempool += itempool

