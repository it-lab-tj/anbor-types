from typing import Annotated

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
