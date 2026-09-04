from typing import Annotated, Optional

from anbor_types import ID_T, ListQuery, Query
from anbor_types.api.annotated import ATSearch
from anbor_types.api.constants import ID_MAX
from anbor_types.api.filter_specs import AFStatus
from anbor_types.api.queries import ShortListQuery
from anbor_types.api.types import OrderingAllowedFieldsT
from anbor_types.common.annotated import ATDatetimeRN
from anbor_types.utils.filter.meta import FilterMeta, FilterSpec
from anbor_types.utils.mixins import OrderingQueryMixin


class JobPositionShortListQuery(ShortListQuery): ...


class JobPositionListQuery(ListQuery, OrderingQueryMixin, metaclass=FilterMeta):
    _ordering_allowed_fields: OrderingAllowedFieldsT = {"created_at", "name"}

    # Prefix search on the position name.
    search: Annotated[Optional[ATSearch], FilterSpec.string()] = None

    status: AFStatus

    # Positions that grant this permission -- "who can do X?", which is the
    # question an admin actually asks. Compiles to EXISTS over the grant table.
    permission_id: Annotated[ID_T, FilterSpec.numeric(int, lte=ID_MAX)]

    # Positions held by this user (EXISTS over user_job_position); a user may
    # hold several.
    user_id: Annotated[ID_T, FilterSpec.numeric(int, lte=ID_MAX)]

    created_at__rn: ATDatetimeRN


class JobPositionDetailedQuery(Query):
    id: ID_T


class PermissionCatalogQuery(Query):
    """The whole catalog, grouped by boundary -- what a permission matrix needs
    to render before anything is ticked. Static, so it is cacheable."""


class StaffJobPositionsQuery(Query):
    """Positions held by one user, and the permissions they union up to."""

    user_id: ID_T
