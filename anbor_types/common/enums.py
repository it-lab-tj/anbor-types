from enum import IntEnum, StrEnum


class StatusEnum(IntEnum):
    ACTIVE = 1
    INACTIVE = 0


class ContentTypeEnum(StrEnum):
    COUNTERPARTY = "storage_counterparty"
