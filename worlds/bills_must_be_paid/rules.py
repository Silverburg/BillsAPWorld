from __future__ import annotations
from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule
from .data.data_locations import LOCATION_LIST
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
    location_3 = world.get_location("PIG_3")
    world.set_rule(location_3, Has(PROG_PIG,1))

    location_5 = world.get_location("PIG_5")
    world.set_rule(location_5, Has(PROG_PIG,2))

def set_completion_condition(world: BillsAPWorld) -> None:
    world.set_completion_rule(Has(PROG_PIG,3))