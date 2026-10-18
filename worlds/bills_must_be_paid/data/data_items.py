from BaseClasses import ItemClassification

PROG_PIG = "Progressive Piggy"
PROG_HAM = "Progressive Hammer"
PROG_ACC = "Progressive Accessory"

FILLER = "Filler"
TRAP = "Trap"

ID_KEY = "id_key"
CLASSIFICATION = "classification"
AMOUNT = "amount"

ITEM_LIST = {
    PROG_PIG: {
        ID_KEY: 1,
        CLASSIFICATION: ItemClassification.progression,
        AMOUNT: 3
    },
    PROG_HAM: {
        ID_KEY: 2,
        CLASSIFICATION: ItemClassification.progression,
        AMOUNT: 2
    },
    PROG_ACC: {
        ID_KEY: 3,
        CLASSIFICATION: ItemClassification.filler,
        AMOUNT: 2
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
