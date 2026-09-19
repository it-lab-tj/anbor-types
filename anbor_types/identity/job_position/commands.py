from typing import List

from pydantic import Field

from anbor_types import ID_T, Command
from anbor_types.identity.job_position.dto import JobPositionWriteDTO


class JobPositionCreateCommand(JobPositionWriteDTO, Command): ...


class JobPositionUpdateCommand(JobPositionWriteDTO, Command):
    """Same payload as create: the client submits the position's full intended
    state -- name, permissions and object scopes -- and the server replaces all
    three in one transaction."""

    id: ID_T


class JobPositionToggleStatusCommand(Command):
    id: ID_T


class JobPositionDeleteCommand(Command):
    id: ID_T


class StaffJobPositionsSetCommand(Command):
    """Replaces the full set of positions one user holds.

    Membership is owned from the user side only. Editing a position never
    changes who holds it, so two admins on different screens cannot silently
    unassign each other's people.
    """

    user_id: ID_T
    job_position_ids: List[ID_T] = Field(default_factory=list)
