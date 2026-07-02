from typing import Annotated, Tuple
from pydantic import StringConstraints
from anbor_types.utils.filter.meta import FilterSpec

type AFSearch = Annotated[ATSearch, FilterSpec.string()]


type ATSearch = Annotated[
    str,
    StringConstraints(
        max_length=100,
        strip_whitespace=True,
    ),
]


type ATOrdering = Annotated[
    Tuple[str],
    StringConstraints(
        max_length=100,
    ),
]
