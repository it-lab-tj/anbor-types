from datetime import datetime
from typing import Annotated, Optional, Tuple


from anbor_types import Query
from anbor_types.utils.filter.meta import FilterMeta
from anbor_types.utils.filter.types import FilterSpec


class WalletIncomeStatementQuery(Query, metaclass=FilterMeta):
    date__rn: Annotated[
        Tuple[Optional[datetime.date], Optional[datetime.date]],
        FilterSpec.date_range(),
    ]
