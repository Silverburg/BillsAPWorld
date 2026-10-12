from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle

class TrapChance(Range):
    """
    Percentage chance of traps.
    """

    display_name = "Trap Chance"

    range_start = 0
    range_end = 100
    default = 0

@dataclass
class BillsAPOptions(PerGameCommonOptions):
    trap_chance: TrapChance

option_groups = [
    OptionGroup(
        "Initial Group",
        [TrapChance]
        )
    # OptionGroup(
    #     "Secondary Group",
    #     [OptionClassesHere]
    #     )
]