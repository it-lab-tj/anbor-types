from pydantic import BaseModel, ConfigDict, Field

from anbor_types.api import const
from typing import (
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
Pipeline: TypeAlias = Callable[
    [Callable[..., Awaitable[Any]]], Callable[..., Awaitable[Any]]
]
ListLike: TypeAlias = Union[Sequence, Set]


class FactoryT(Protocol[T]):
    def __call__(self) -> T | Awaitable[T]: ...


class BasePydanticModel(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)


class Query(BaseModel):
    """
    The same as 'Command' class. But just standard for query-only use(get requests).
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid", frozen=True)


class ListQuery(Query):
    limit: int = Field(
        default=const.DEFAULT_LIMIT,
        gt=const.MIN_LIMIT - 1,
        lt=const.MAX_LIMIT + 1,
    )
    offset: int = Field(default=const.DEFAULT_OFFSET, gt=const.MIN_OFFSET - 1)


class Command(BaseModel):
    """
    Base class for creating commands for mediator.
    Inherit and use with mediator.
    """

    model_config = ConfigDict(arbitrary_types_allowed=True, extra="forbid", frozen=True)
