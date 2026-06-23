from datetime import datetime
from typing import Annotated

from pydantic import Field, constr

from anbor_types.handbook.constraints import (
    PROMOTION_NAME_MAX_LENGTH,
    PROMOTION_NAME_MIN_LENGTH,
)

type ATPromotionName = Annotated[
    str,
    constr(max_length=PROMOTION_NAME_MAX_LENGTH, min_length=PROMOTION_NAME_MIN_LENGTH),
]


type ATPromotionStart = Annotated[
    datetime,
    Field(
        ge=datetime(2000, 1, 1),
        le=datetime(2099, 12, 31),
    ),
]


type ATPromotionEnd = Annotated[
    datetime,
    Field(
        ge=datetime(2000, 1, 1),
        le=datetime(2099, 12, 31),
    ),
]
