from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups
from .constants import GAME_NAME

class BillsAPWebWorld(WebWorld):
    game = GAME_NAME

    theme = "stone"

    setup_en = Tutorial(
        "Bills Must Be Paid AP Setup Guide",
        "A guide to setting up Bills Must Be Paid for MultiWorld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Silverburg"]
        )

    tutorials = [setup_en]
    option_groups = option_groups