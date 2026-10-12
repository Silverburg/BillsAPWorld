from BaseClasses import ItemClassification
from ..constants import *

ITEM_1 = "Item 1"
ITEM_2 = "Item 2"
ITEM_3 = "Item 3"

FILLER = "Filler"
TRAP = "Trap"

ITEM_LIST = {
    ITEM_1: {
        ID_KEY: 1,
        CLASSIFICATION: ItemClassification.progression
    },
    ITEM_2: {
        ID_KEY: 2,
        CLASSIFICATION: ItemClassification.progression
    },
    ITEM_3: {
        ID_KEY: 3,
        CLASSIFICATION: ItemClassification.progression
    },
    FILLER: {
        ID_KEY: 4,
        CLASSIFICATION: ItemClassification.filler
    },
    TRAP: {
        ID_KEY: 5,
        CLASSIFICATION: ItemClassification.trap
    }
}
