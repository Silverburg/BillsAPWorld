from __future__ import annotations
from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule
from .data.data_locations import *
from .data.data_items import *

if TYPE_CHECKING:
    from .world import BillsAPWorld

def set_all_rules(world: BillsAPWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: BillsAPWorld) -> None:
    #No entrance rules as of yet
    pass

def set_all_location_rules(world: BillsAPWorld) -> None:
    for loc in LOCATION_LIST:
        if LOCATION_LIST[loc][LOC_TYPE] == "piggy":
            location = world.get_location(loc)
            world.set_rule(location, Has(PROG_PIG,LOCATION_LIST[loc][ID_KEY]))
    # location_3 = world.get_location("Unlock The Tourist")
    # world.set_rule(location_3, Has(PROG_PIG,1))

    # location_5 = world.get_location("Unlock Goblig")
    # world.set_rule(location_5, Has(PROG_PIG,2))

def set_completion_condition(world: BillsAPWorld) -> None:
    world.set_completion_rule(Has(PROG_PIG,3))