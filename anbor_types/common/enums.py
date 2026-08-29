from enum import IntEnum, StrEnum


class StatusEnum(IntEnum):
    ACTIVE = 1
    INACTIVE = 0


class ContentTypeEnum(StrEnum):
    COUNTERPARTY = "storage_counterparty"
    CASH_DESK = "handbook_cashdesk"
    CASH_DESK_REBALANCE_HISTORY = "handbook_cashdeskrebalancehistory"
    SUBJECT_REBALANCE_HISTORY = "warehouse_subjectrebalance"
    USER = "accounts_user"
    COMPANY = "company_company"
    STOCK_OPERATION = "warehouse_stockoperation"
    SERVICE = "handbook_service"
    PRODUCT = "handbook_product"
    STOCK_OPERATION_GROUP = "storage_stockoperationgroup"
