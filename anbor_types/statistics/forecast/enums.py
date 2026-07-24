from enum import StrEnum


class PurchaseHorizonEnum(StrEnum):
    """Restock planning horizon for the purchase-suggestion read model."""

    WEEK = "week"
    MONTH = "month"
