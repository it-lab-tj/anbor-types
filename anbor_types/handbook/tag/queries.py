from typing import Optional, Annotated

from anbor_types.utils.filter.types import FilterSpec

from anbor_types import ListQuery
from anbor_types.api.annotated import ATSearch
from anbor_types.api.filter_specs import AFStatus
from anbor_types.api.queries import ShortListQuery
from anbor_types.utils.filter import FilterMeta


class TagListQuery(ListQuery, metaclass=FilterMeta):
    search: Annotated[Optional[ATSearch], FilterSpec.string()] = None
    status: AFStatus


class TagShortListQuery(ShortListQuery): ...
