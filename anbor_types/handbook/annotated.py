from typing import Annotated

from pydantic import Field, constr

from anbor_types.common.annotated import ATDatetime
from anbor_types.common.constraints import DATETIME_MAX, DATETIME_MIN
from anbor_types.handbook.constraints import (
    PROMOTION_NAME_MAX_LENGTH,
    PROMOTION_NAME_MIN_LENGTH,
)

type ATPromotionName = Annotated[
    str,
    constr(max_length=PROMOTION_NAME_MAX_LENGTH, min_length=PROMOTION_NAME_MIN_LENGTH),
]


type ATPromotionStart = Annotated[
    ATDatetime,
    Field(
        ge=DATETIME_MIN,
        le=DATETIME_MAX,
    ),
]


type ATPromotionEnd = Annotated[
    ATDatetime,
    Field(
        ge=DATETIME_MIN,
        le=DATETIME_MAX,
    ),
]
