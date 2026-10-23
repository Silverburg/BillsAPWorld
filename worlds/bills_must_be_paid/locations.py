from __future__ import annotations
from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location
from .data.data_locations import *
from .data.data_regions import *
from .constants import GAME_NAME

from . import items

if TYPE_CHECKING:
    from .world import BillsAPWorld

class BillsAPLocation(Location):
    game = GAME_NAME

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_LIST[location_name][ID_KEY] for location_name in location_names}

def create_all_locations(world: BillsAPWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: BillsAPWorld) -> None:
    main_area = world.get_region(PHASE_1)

    for location, values in LOCATION_LIST.items():
        loc = BillsAPLocation(world.player, location, values[ID_KEY], main_area)
        main_area.locations.append(loc)

def create_events(world: BillsAPWorld) -> None:
    pass