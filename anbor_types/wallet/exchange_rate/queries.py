from anbor_types import ListQuery
from anbor_types.api.filter_specs import AFStatus
from anbor_types.utils.filter.meta import FilterMeta


class ExchangeRateShortListQuery(ListQuery, metaclass=FilterMeta):
    status: AFStatus
