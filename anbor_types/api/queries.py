from typing import Annotated, Optional

from anbor_types import ListQuery
from anbor_types.api.annotated import ATSearch
from anbor_types.api.filter_specs import AFStatus
from anbor_types.utils.filter.meta import FilterMeta, FilterSpec


class ShortListQuery(ListQuery, metaclass=FilterMeta):
    """Base query for `/short` reference endpoints:
    limit/offset + optional prefix search + status filter.

    Note: `Optional[AFSearch]` is not used here on purpose — wrapping
    `Annotated` into `Optional` hides `FilterSpec` from both `FilterMeta`
    and the filter parser, so such a field never compiles into a filter.
    """

    search: Annotated[Optional[ATSearch], FilterSpec.string()] = None
    status: AFStatus
