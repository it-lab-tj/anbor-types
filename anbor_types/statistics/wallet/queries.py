from typing import Annotated, Optional, Tuple

from anbor_types.common.annotated import ATDatetime

from anbor_types import ID_T, Query
from anbor_types.utils.filter.meta import FilterMeta
from anbor_types.utils.filter.types import FilterSpec


class WalletIncomeStatementQuery(Query, metaclass=FilterMeta):
    date__rn: Annotated[
        Tuple[Optional[ATDatetime], Optional[ATDatetime]],
        FilterSpec.datetime_range(both_required=True),
    ]

    project_id: Optional[ID_T] = None
