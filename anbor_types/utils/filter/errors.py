"""Filter validation failures, expressed in pydantic's own terms.

``FilterValidator`` runs inside a pydantic core validator, so the failures it
reports belong in pydantic's error channel. Raising anything that is not a
``ValueError`` there escapes the validation pipeline entirely: pydantic stops
collecting, the offending field loses its ``loc``, and the caller is told about
one bad filter when three were sent.

``PydanticCustomError`` is a ``ValueError``, so a violation raised through
``raise_violations`` is caught, tagged with the field it came from, and
aggregated with every other field's errors into a single ``ValidationError``.
"""

from enum import Enum
from typing import Any, Dict, List, NamedTuple, NoReturn

from pydantic_core import PydanticCustomError


class FilterErrorType(str, Enum):
    """``type`` of a filter error, as it appears in ``ValidationError.errors()``."""

    REQUIRED = "filter_required"
    INVALID_VALUE = "filter_invalid_value"
    BOUND = "filter_bound"
    RANGE_ORDER = "filter_range_order"
    LENGTH = "filter_length"
    CHOICES = "filter_choices"
    DUPLICATED = "filter_duplicated"


class FilterViolation(NamedTuple):
    """One thing wrong with one filter value."""

    type: FilterErrorType
    message: str
    context: Dict[str, Any]


def raise_violations(violations: List[FilterViolation], lookup: Any) -> NoReturn:
    """Report the violations collected for a single filter.

    Pydantic keeps one error per field, so everything wrong with this filter
    travels together under ``ctx["violations"]``; the first violation supplies
    the error's ``type`` and ``msg`` so the common single-fault case reads
    naturally. Pydantic then aggregates across fields on its own.
    """
    first = violations[0]
    raise PydanticCustomError(
        first.type.value,
        first.message,
        {
            "lookup": lookup.value if isinstance(lookup, Enum) else lookup,
            "violations": [
                {"type": v.type.value, "message": v.message, **v.context}
                for v in violations
            ],
        },
    )
