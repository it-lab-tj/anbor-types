from typing import Annotated, Optional, Tuple

from anbor_types.common.annotated import ATDatetime

from anbor_types import Query, ID_T
from anbor_types.utils.filter.meta import FilterMeta
from anbor_types.utils.filter.types import FilterSpec
from anbor_types.api.constants import ID_MAX


class WalletIncomeStatementQuery(Query, metaclass=FilterMeta):
    date__rn: Annotated[
        Tuple[Optional[ATDatetime], Optional[ATDatetime]],
        FilterSpec.datetime_range(both_required=True),
    ]
    project_id: Annotated[
        Optional[ID_T],
        FilterSpec.numeric(
            int,
            lte=ID_MAX,
        ),
    ]
