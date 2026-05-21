from decimal import Decimal
from typing import Annotated, TypeAlias

from pydantic import Field, constr, StringConstraints
from pydantic.functional_validators import BeforeValidator
from anbor_types.common import constraints as common_constraints
from anbor_types.common.constraints import COMMENT_MAX_LENGTH, MIN_RATE, MAX_RATE
from anbor_types.utils.functions import parse_single_line_str

# ===== Str =====
type ATSingleLineStr = Annotated[str, BeforeValidator(parse_single_line_str)]

type ATInformationStr = Annotated[
    str, constr(max_length=common_constraints.INFORMATION_MAX_LENGTH)
]

type ATComment = Annotated[str, constr(max_length=COMMENT_MAX_LENGTH)]


# ===== Decimal =====
type ATPrice = Annotated[
    Decimal,
    Field(
        max_digits=common_constraints.DECIMAL_PRICE_DIGITS,
        decimal_places=common_constraints.DECIMAL_PRICE_PLACES,
    ),
]
type ATDiscount = Annotated[
    Decimal,
    Field(
        max_digits=common_constraints.DECIMAL_DISCOUNT_DIGITS,
        decimal_places=common_constraints.DECIMAL_DISCOUNT_PLACES,
        le=Decimal("100"),
        default=Decimal("0"),
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
    lambda x: x[:-1] if x[-1] == "/" else x,
]
