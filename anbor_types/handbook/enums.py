from enum import IntEnum, StrEnum


class OperatingExpenseTypeEnum(IntEnum):
    EXPENSE = 0
    INCOME = 1
    TRANSFER = 2


# Promotion Items
class PromotionItemConditionsEnum(IntEnum):
    THRESHOLD_AMOUNT = 1
    THRESHOLD_PRICE = 2
    BUY_X = 3
    ANYWAY = 4


class PromotionItemAwardsEnum(IntEnum):
    PERCENT_DISCOUNT = 1
    FIXED_DISCOUNT = 2
    FIXED_PRICE = 3
    GIFT = 4
    BUNDLE = 5
    QUANTITY_DISCOUNT = 6
    PROMOCODE = 7
    BONUS = 8


# Tag
class TagDefaultNameStrEnum(StrEnum):
    NEW = "Новый"
    IN_PROGRESS = "В работе"
    COMPLETED = "Выполнен"
    ON_HOLD = "Приостановлена"
    CANCELLED = "Отменена"
