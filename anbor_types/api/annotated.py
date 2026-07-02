from typing import Annotated
from pydantic import StringConstraints

type ATSearch = Annotated[
    str,
    StringConstraints(
        max_length=100,
        strip_whitespace=True,
    ),
]
