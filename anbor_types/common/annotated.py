from datetime import datetime
from decimal import Decimal
from typing import Annotated, Optional, Tuple, TypeAlias, List

from anbor_types import ID_T
from pydantic import AfterValidator, Field, StringConstraints
from pydantic.functional_validators import BeforeValidator

from anbor_types.api.constants import DECIMAL_ZERO, PRICE_MAX
from anbor_types.common import constraints as common_constraints
from anbor_types.common.constraints import (
    COMMENT_MAX_LENGTH,
    DATETIME_MAX,
    MIN_RATE,
    MAX_RATE,
    DISCOUNT_MAX,
    DESCRIPTION_MAX_LENGTH,
    APP_VERSION_REGEX,
)
from anbor_types.utils.filter.types import FilterSpec
from anbor_types.utils.functions import (
    set_timezone,
    parse_single_line_str,
    default_utc_now,
)
from anbor_types.common.constraints import (
    ADDRESS_MAX_LENGTH,
    ADDRESS_REGEX,
    PASSWORD_MAX_LENGTH,
    PASSWORD_MIN_LENGTH,
)
from anbor_types.utils.validators import regex_validator_factory

# ===== Str =====
type ATSingleLineStr = Annotated[str, BeforeValidator(parse_single_line_str)]

type ATAppVersion = Annotated[
    str,
    StringConstraints(
        max_length=11,
    ),
    AfterValidator(
        regex_validator_factory(APP_VERSION_REGEX),
    ),
    BeforeValidator(parse_single_line_str),
]

type ATInformationStr = Annotated[
    str, StringConstraints(max_length=common_constraints.INFORMATION_MAX_LENGTH)
]

type ATComment = Annotated[str, StringConstraints(max_length=COMMENT_MAX_LENGTH)]

type ATAddress = Annotated[
    str,
    StringConstraints(max_length=ADDRESS_MAX_LENGTH, strip_whitespace=True),
    regex_validator_factory(ADDRESS_REGEX, normalize=True),
]

type ATDescription = Annotated[
    str,
    StringConstraints(
        max_length=DESCRIPTION_MAX_LENGTH,
        strip_whitespace=True,
    ),
]

type ATPassword = Annotated[
    str,
    StringConstraints(
        min_length=PASSWORD_MIN_LENGTH,
        max_length=PASSWORD_MAX_LENGTH,
        strip_whitespace=True,
    ),
]

# ===== Decimal =====
type ATPrice = Annotated[
    Decimal,
    Field(
        max_digits=common_constraints.DECIMAL_PRICE_DIGITS,
        decimal_places=common_constraints.DECIMAL_PRICE_PLACES,
        ge=DECIMAL_ZERO,
        le=PRICE_MAX,
    ),
]
type ATDiscount = Annotated[
    Decimal,
    Field(
        max_digits=common_constraints.DECIMAL_DISCOUNT_DIGITS,
        decimal_places=common_constraints.DECIMAL_DISCOUNT_PLACES,
        ge=DECIMAL_ZERO,
        le=DISCOUNT_MAX,
    ),
]
ATBalance: TypeAlias = Annotated[
    Decimal,
    Field(
        max_digits=common_constraints.DECIMAL_BALANCE_DIGITS,
        decimal_places=common_constraints.DECIMAL_BALANCE_PLACES,
    ),
]

type ATRate = Annotated[Decimal, Field(gt=MIN_RATE, le=MAX_RATE)]

# ===== HTTP =====
type ATDomainName = Annotated[
    str,
    StringConstraints(
        max_length=253,
        min_length=4,
        pattern=r"^(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,6}$",
        strip_whitespace=True,
    ),
    # TOFIX: a bare callable here is dropped -- the trailing slash is never stripped.
    lambda x: x[:-1] if x[-1] == "/" else x,
]

type ATFileIds = Annotated[
    List[ID_T], Field(max_length=common_constraints.FILE_IDS_MAX_COUNT)
]

# ====== Date =======
type ATDatetime = Annotated[datetime, AfterValidator(set_timezone)]
type ATDatetimeDefault = Annotated[
    datetime, BeforeValidator(default_utc_now), AfterValidator(set_timezone)
]


ATDatetimeRN = Annotated[
    Tuple[Optional[ATDatetime], Optional[ATDatetime]],
    FilterSpec.datetime_range(
        lte=DATETIME_MAX,
    ),
]


# ======= For Filters =====
type ATFilterRange[T] = Tuple[Optional[T], Optional[T]]
type ATFilterRangeRequired[T] = Tuple[T, T]
