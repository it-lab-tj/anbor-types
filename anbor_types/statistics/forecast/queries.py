from anbor_types import ListQuery
from anbor_types.statistics.forecast.enums import PurchaseHorizonEnum


class ProductPurchaseSuggestionListQuery(ListQuery):
    """Top product variants to restock, ranked by recommended buy quantity.

    ``horizon`` selects the forecast window (7 or 30 days); ``limit``/``offset``
    are inherited from ``ListQuery``.
    """

    horizon: PurchaseHorizonEnum = PurchaseHorizonEnum.WEEK
