from datetime import datetime
from typing import List, Optional

import msgspec
from pydantic import Field

from anbor_types import ID_T, BasePydanticModel
from anbor_types.common.dto import NameIdDTO
from anbor_types.common.enums import StatusEnum


class JobPositionObjectScopeInputDTO(BasePydanticModel):
    """Object ids one scopable boundary is narrowed to.

    Only meaningful when `permission_ids` also contains that boundary's
    object-scope marker; without it the position already covers every object
    and these ids would be dead rows.
    """

    boundary: str = Field(min_length=1, max_length=64)
    object_ids: List[ID_T] = Field(default_factory=list)


class JobPositionWriteDTO(BasePydanticModel):
    """Full intended state of a position. POST and PUT take the same shape.

    Everything here is a full-state replace, not a patch: the permission screen
    submits what it shows, and anything absent is revoked. `object_scopes` is
    part of the same write so a permission and the objects it applies to land
    in one transaction -- they are meaningless apart.

    Staff membership is deliberately NOT here; it is written from the staff
    member's side, so this screen cannot unassign people by omitting a field
    it never displayed.
    """

    name: str = Field(min_length=1, max_length=100)
    permission_ids: List[ID_T] = Field(default_factory=list)
    object_scopes: List[JobPositionObjectScopeInputDTO] = Field(default_factory=list)


class PermissionDTO(msgspec.Struct):
    """One permission as the catalog defines it. Static data -- ids are a
    declared contract, not a sequence, so the client may cache this.

    No display text: a permission is a boundary, an action and an id, and how
    that is worded to a user is the client's business. `codename`
    (`<boundary>.<action>`) is the key a translation table is keyed by.
    """

    id: ID_T
    codename: str
    boundary: str
    action: str
    # Ids this permission pulls in when granted. The UI should tick these too,
    # so what the user sees matches what the server will store.
    requires: List[ID_T]


class PermissionBoundaryDTO(msgspec.Struct):
    """A boundary with its permissions -- the shape a permission matrix renders.

    `scopable` says whether this boundary supports object-level narrowing; when
    true, `object_scope_permission_id` is the marker to send alongside the
    chosen object ids.
    """

    # No display text here either -- `code` is what a client-side translation
    # table is keyed by. `order` is the catalog's declaration order, so a
    # client can render boundaries the way the product groups them.
    code: str
    order: int
    scopable: bool
    object_scope_permission_id: Optional[ID_T]
    permissions: List[PermissionDTO]


class JobPositionShortListDTO(msgspec.Struct):
    id: ID_T
    name: str


class JobPositionListDTO(msgspec.Struct):
    id: ID_T
    name: str
    status: StatusEnum
    created_at: datetime
    # Counts, not the collections themselves: a list screen must not pay for
    # loading every permission of every position.
    permission_count: int
    staff_count: int


class JobPositionObjectScopeDTO(msgspec.Struct):
    """Object ids a scoped boundary is limited to, for one position."""

    boundary: str
    object_ids: List[ID_T]


class JobPositionDetailedDTO(msgspec.Struct):
    id: ID_T
    name: str
    status: StatusEnum
    created_at: datetime
    updated_at: Optional[datetime]

    # The stored grant set, already dependency-expanded on write.
    permission_ids: List[ID_T]

    object_scopes: List[JobPositionObjectScopeDTO]
    staff: List[NameIdDTO]

class StaffJobPositionsDTO(msgspec.Struct):
    """One user's positions and what they add up to.

    A user may hold several positions and positions only ever grant, so
    `permission_ids` is the UNION across them -- computed here because the
    client cannot union two positions without the dependency graph.
    """

    user_id: ID_T
    job_positions: List[NameIdDTO]
    permission_ids: List[ID_T]
    object_scopes: List[JobPositionObjectScopeDTO]