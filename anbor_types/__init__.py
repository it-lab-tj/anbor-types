from decimal import Decimal

import msgspec
from pydantic import BaseModel, ConfigDict, Field, GetJsonSchemaHandler
from pydantic.json_schema import JsonSchemaValue
from pydantic_core import CoreSchema

from anbor_types.api import constants
from typing import (
    Generic,
    List,
    TypeAlias,
    Callable,
    Awaitable,
    Any,
    TypeVar,
    Protocol,
    Union,
    Sequence,
    Set,
)

T = TypeVar("T")
ID_T: TypeAlias = int
type Numeric = Union[int, float, Decimal]
Pipeline: TypeAlias = Callable[
    [Callable[..., Awaitable[Any]]], Callable[..., Awaitable[Any]]
]
type ListLike[T: Any] = Union[Sequence[T], Set[T]]


class FactoryT(Protocol[T]):
    def __call__(self) -> T | Awaitable[T]: ...


class BasePydanticModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True, populate_by_name=True)


class Query(BaseModel):
    """
    The same as 'Command' class. But just standard for query-only use(get requests).
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="ignore")


class ListQuery(Query):
    limit: int = Field(
        default=constants.DEFAULT_LIMIT,
        gt=constants.MIN_LIMIT - 1,
        lt=constants.MAX_LIMIT + 1,
    )
    offset: int = Field(default=constants.DEFAULT_OFFSET, gt=constants.MIN_OFFSET - 1)

    model_config = ConfigDict(extra="ignore")

    @classmethod
    def __get_pydantic_json_schema__(
        cls,
        core_schema: CoreSchema,
        handler: GetJsonSchemaHandler,
    ) -> JsonSchemaValue:
        schema = handler(core_schema)

        properties = schema.setdefault("properties", {})

        if "limit" in properties:
            properties["limit"].update(
                {
                    "title": "Limit",
                    "description": (
                        f"Maximum number of items to return. "
                        f"Allowed range: {constants.MIN_LIMIT}–{constants.MAX_LIMIT}. "
                        f"Default: {constants.DEFAULT_LIMIT}."
                    ),
                    "example": constants.DEFAULT_LIMIT,
                }
            )

        if "offset" in properties:
            properties["offset"].update(
                {
                    "title": "Offset",
                    "description": (
                        "Number of items to skip before returning results. "
                        f"Minimum: {constants.MIN_OFFSET}. "
                        f"Default: {constants.DEFAULT_OFFSET}."
                    ),
                    "example": constants.DEFAULT_OFFSET,
                }
            )

        return schema


class ListQueryResponse(msgspec.Struct, Generic[T]):
    count: int
    rows: List[T]

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid", frozen=True)


class Command(BaseModel):
    """
    Base class for creating commands for mediator.
    Inherit and use with mediator.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="ignore", frozen=True)
