from typing import Any

from pydantic import Field

from anbor_types import Query


class DailyAnalyticListQuery(Query):
    filters: Any = Field(default_factory=tuple, init=False)
