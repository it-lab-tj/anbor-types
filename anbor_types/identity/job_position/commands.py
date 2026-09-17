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
