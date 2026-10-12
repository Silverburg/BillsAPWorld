from __future__ import annotations
from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region
from .data.data_regions import *

if TYPE_CHECKING:
    from .world import BillsAPWorld

def create_and_connect_regions(world: BillsAPWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: BillsAPWorld) -> None:
    main_area = Region(MAIN_AREA, world.player, world.multiworld)

    regions = [main_area]

    world.multiworld.regions += regions

def connect_regions(world: BillsAPWorld) -> None:
    #Only one region right now, continuing.
    pass