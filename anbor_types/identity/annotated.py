from typing import Annotated

from pydantic import EmailStr, StringConstraints

from anbor_types.identity.constraints import (
    COMPANY_NICK_MAX_LENGTH,
    COMPANY_NICK_MIN_LENGTH,
    OTP_MAX_LENGTH,
    OTP_MIN_LENGTH,
    OTP_REGEX,
    ROLE_NAME_MAX_LENGTH,
    ROLE_NAME_MIN_LENGTH,
    ROLE_NAME_REGEX,
    USER_NAME_MAX_LENGTH,
    USER_NAME_MIN_LENGTH,
    USER_NAME_REGEX,
    USER_PHONE_MAX_LENGTH,
    USER_PHONE_MIN_LENGTH,
    USER_PHONE_REGEX,
    USER_USERNAME_MAX_LENGTH,
    USER_USERNAME_MIN_LENGTH,
    USER_USERNAME_REGEX,
)
from anbor_types.utils.validators import regex_validator_factory

# TOFIX: bare callables in Annotated are dropped by pydantic, so every
# regex_validator_factory below is inert -- see docs/architecture/validation.md.


type ATUserName = Annotated[
    str,
    StringConstraints(
        min_length=USER_NAME_MIN_LENGTH,
        max_length=USER_NAME_MAX_LENGTH,
        strip_whitespace=True,
    ),
    regex_validator_factory(USER_NAME_REGEX, normalize=True),
]


type ATUserUsername = Annotated[
    str,
    StringConstraints(
        min_length=USER_USERNAME_MIN_LENGTH,
        max_length=USER_USERNAME_MAX_LENGTH,
        strip_whitespace=True,
    ),
    regex_validator_factory(USER_USERNAME_REGEX, normalize=True),
]


type ATEmail = Annotated[str, EmailStr]

type ATPhone = Annotated[
    str,
    StringConstraints(
        min_length=USER_PHONE_MIN_LENGTH,
        max_length=USER_PHONE_MAX_LENGTH,
        pattern=USER_PHONE_REGEX.pattern,
        strip_whitespace=True,
    ),
]

type ATRoleName = Annotated[
    str,
    StringConstraints(
        max_length=ROLE_NAME_MAX_LENGTH,
        min_length=ROLE_NAME_MIN_LENGTH,
        strip_whitespace=True,
    ),
    regex_validator_factory(ROLE_NAME_REGEX, normalize=True),
]

type ATCompanyNick = Annotated[
    str,
    StringConstraints(
        max_length=COMPANY_NICK_MAX_LENGTH,
        min_length=COMPANY_NICK_MIN_LENGTH,
        strip_whitespace=True,
    ),
]

type ATCompanyName = Annotated[
    str,
    StringConstraints(
        max_length=COMPANY_NICK_MAX_LENGTH,
        min_length=COMPANY_NICK_MIN_LENGTH,
        strip_whitespace=True,
    ),
]

type ATOtp = Annotated[
    str,
    StringConstraints(
        min_length=OTP_MIN_LENGTH,
        max_length=OTP_MAX_LENGTH,
        strip_whitespace=True,
    ),
    regex_validator_factory(OTP_REGEX),
]
