from typing import Annotated

from pydantic import StringConstraints

from anbor_types import ID_T, BasePydanticModel, Command
from anbor_types.common.annotated import ATPassword
from anbor_types.identity.constants import OtpKindEnum
from anbor_types.identity.user.dto import (
    StaffMemberCreateDTO,
    StaffMemberUpdateDTO,
    UserConfirmationRequestDTO,
    UserAuthMeta,
)
from anbor_types.identity.annotated import ATUserUsername

# --------------------------------------------------------------------------- #
# Common, kind-agnostic user commands
# (reusable by any user kind, not just staff)
# --------------------------------------------------------------------------- #


class UserConfirmationCommand(UserConfirmationRequestDTO, Command):
    """Confirm a one-time code for a user.

    `kind` is set by the route, not the request body — otherwise a caller could
    present an invitation token as, say, a phone confirmation and trigger the
    wrong side effect.
    """

    kind: OtpKindEnum


class UserResendConfirmationCommand(Command):
    user_id: ID_T


class UserToggleStatusCommand(Command):
    id: ID_T


class UserLoginCommand(Command):
    username: ATUserUsername
    password: ATPassword
    meta: UserAuthMeta


class UserSessionRefreshCommand(Command):
    refresh: Annotated[
        str,
        StringConstraints(max_length=1000, ascii_only=True, strip_whitespace=True),
    ]

    meta: UserAuthMeta


# --------------------------------------------------------------------------- #
# Staff-specific management commands
# --------------------------------------------------------------------------- #


class StaffMemberCreateCommand(StaffMemberCreateDTO, Command): ...


class StaffMemberUpdateCommand(StaffMemberUpdateDTO, Command):
    id: ID_T


class StaffMemberDeleteCommand(BasePydanticModel, Command):
    id: ID_T
