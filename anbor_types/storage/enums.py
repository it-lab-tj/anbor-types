from enum import IntEnum


class SOGAction(IntEnum):
    SALE = 0, "Продажа"
    RECEIPT = 1, "Прием"
    TRANSFER = 2, "Передача"
    RECEIPTING = 3, "Receipting"
