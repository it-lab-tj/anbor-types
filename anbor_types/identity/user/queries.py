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


class StaffMemberShortListQuery(ShortListQuery): ...


class StaffMemberListQuery(ListQuery, OrderingQueryMixin, metaclass=FilterMeta):
    _ordering_allowed_fields: OrderingAllowedFieldsT = {"created_at"}

    # Search compiles against profile first/last name + username (see the
    # StaffMemberFilterCompiler on the data-access side).
    search: Annotated[Optional[ATSearch], FilterSpec.string()] = None

    status: AFStatus

    # Filters staff assigned to this job position (join to user_job_position).
    job_position_id: Annotated[
        ID_T,
        FilterSpec.numeric(int, lte=ID_MAX),
    ]

    created_at__rn: ATDatetimeRN


class StaffMemberDetailedQuery(Query):
    id: ID_T
