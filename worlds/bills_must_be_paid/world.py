from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World
from .data.data_locations import *
from .data.data_items import *
from .data.data_regions import *

from . import items, locations, regions, rules, web_world, constants
from . import options as billsap_options

class BillsAPWorld(World):
    """
    Update docstring of game details here.
    """

    game = constants.GAME_NAME
    web = web_world.BillsAPWebWorld()

    options_dataclass = billsap_options.BillsAPOptions
    options: billsap_options.BillsAPOptions

    location_name_to_id = {name: values[ID_KEY] for name, values in LOCATION_LIST.items()}
    item_name_to_id = {name: values[ID_KEY] for name, values in ITEM_LIST.items()}

    origin_region_name = PHASE_1

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.BillsAPItem:
            item = ITEM_LIST[name]
            return items.BillsAPItem(name, item[CLASSIFICATION], item[ID_KEY], self.player)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        #Not currently needed, but leaving here for future reference.
        #return self.options.as_dict()
        pass