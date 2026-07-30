from anbor_types import ListQuery, Query
from anbor_types.common.annotated import ATDatetimeRN
from anbor_types.utils.filter.meta import FilterMeta


class InventoryAnalyticsOverviewQuery(Query): ...


class InventoryAnalyticsCategoryFlowQuery(Query): ...


class InventoryAnalyticsLiquidQuery(ListQuery): ...


class InventoryAnalyticsIlliquidQuery(ListQuery): ...


class InventoryAnalyticsCashFlowQuery(Query, metaclass=FilterMeta):
    created_at__rn: ATDatetimeRN
