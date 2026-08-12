import datetime
from decimal import Decimal
from typing import Annotated, Optional, Tuple


from anbor_types import Query
from anbor_types.utils.filter.types import FilterSpec
from anbor_types.utils.filter.meta import FilterMeta


class DailyAnalyticListQuery(Query, metaclass=FilterMeta):
    date: Annotated[
        datetime.date,
        FilterSpec.date(),
    ]

    realisations: Annotated[
        Decimal,
        FilterSpec.numeric(base_type=Decimal),
    ]

    revenues: Annotated[
        Decimal,
        FilterSpec.numeric(base_type=Decimal),
    ]


class WalletCashFlowListQuery(Query, metaclass=FilterMeta):
    date__rn: Annotated[
        Tuple[Optional[datetime.date], Optional[datetime.date]],
        FilterSpec.date_range(both_required=True),
    ]
