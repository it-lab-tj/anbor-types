from anbor_types import ID_T, BasePydanticModel, Command
from anbor_types.identity.user.dto import (
    StaffMemberCreateDTO,
    StaffMemberUpdateDTO,
)


# --------------------------------------------------------------------------- #
# Common, kind-agnostic user-account commands
# (reusable by any user kind, not just staff)
# --------------------------------------------------------------------------- #


class UserConfirmEmailCommand(BasePydanticModel, Command):
    """Confirm a user's email via the base64 token from the invite link."""

    token: str


class UserResendConfirmationCommand(BasePydanticModel, Command):
    user_id: ID_T


class UserToggleStatusCommand(BasePydanticModel, Command):
    id: ID_T


# --------------------------------------------------------------------------- #
# Staff-specific management commands
# --------------------------------------------------------------------------- #


class StaffMemberCreateCommand(StaffMemberCreateDTO, Command): ...


class StaffMemberUpdateCommand(StaffMemberUpdateDTO, Command):
    id: ID_T


class StaffMemberDeleteCommand(BasePydanticModel, Command):
    id: ID_T
