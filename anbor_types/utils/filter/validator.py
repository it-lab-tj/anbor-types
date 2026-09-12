from enum import Enum
from typing import Any, Iterable, List, Optional, Tuple

from anbor_types.utils.filter.enums import FilterLookupEnum
from anbor_types.utils.filter.errors import (
    FilterErrorType,
    FilterViolation,
    raise_violations,
)
from anbor_types.utils.filter.types import FilterSpec

REQUIRED_VALUE_MESSAGE = "Value is required"
INVALID_VALUE_MESSAGE = "Value format is invalid"
DUPLICATED_VALUE_MESSAGE = "Filter value was duplicated"


class FilterValidator:
    """
    Stateless validator for `FilterSpec`.

    Values before validation must exact to `FilterSpec.base_type`
    """

    @classmethod
    def validate(cls, spec: FilterSpec, value: Optional[Any]) -> None:
        if spec.field is None:
            raise RuntimeError("FilterSpec.field must be set before validation")

        elif spec.lookup == FilterLookupEnum.EQ:
            cls._validate_scalar(spec, value)

        elif spec.lookup == FilterLookupEnum.RANGE:
            cls._validate_range(spec, value)

        elif spec.lookup == FilterLookupEnum.IN:
            cls._validate_collection(spec, value)

        elif spec.lookup == FilterLookupEnum.JSON:
            cls._validate_json(spec, value)

        else:
            raise RuntimeError(f"Undefined filter lookup type `{spec.lookup}`")

    @classmethod
    def _raise(cls, spec: FilterSpec, violations: List[FilterViolation]) -> None:
        raise_violations(violations, lookup=spec.lookup)

    @classmethod
    def _validate_scalar(cls, spec: FilterSpec, value: Optional[Any]) -> None:
        if value is None:
            if spec.required:
                cls._raise(spec, [cls._required_violation()])
            return

        violations = cls._validate_bounds(spec, value)
        violations.extend(cls._validate_length(spec, value))
        violations.extend(cls._validate_choices(spec, value))

        if violations:
            cls._raise(spec, violations)

    @classmethod
    def _validate_range(cls, spec: FilterSpec, value: Optional[Any]) -> None:
        if value is None:
            if spec.required:
                cls._raise(spec, [cls._required_violation()])
            return

        if not isinstance(value, (tuple, list)) or len(value) != 2:
            cls._raise(spec, [cls._invalid_value_violation()])

        low, high = value

        if low is None and high is None:
            raise ValueError(
                "Range filter requires at least one boundary. "
                "Use 'value,' for lower bound or ',value' for upper bound."
            )

        if (low is None or high is None) and spec.both_required:
            cls._raise(spec, [cls._required_violation()])

        violations: List[FilterViolation] = []

        if low is not None and high is not None and low > high:
            violations.append(cls._range_order_violation(low, high))

        for endpoint in (low, high):
            if endpoint is not None:
                violations.extend(cls._validate_bounds(spec, endpoint))
                violations.extend(cls._validate_choices(spec, endpoint))

        if violations:
            cls._raise(spec, violations)

    @classmethod
    def _validate_collection(
        cls, spec: FilterSpec, value: Optional[Tuple[Any, ...]]
    ) -> None:
        if value is not None and not isinstance(value, (tuple, list)):
            cls._raise(spec, [cls._invalid_value_violation()])

        if value is None or all(v is None for v in value):
            if spec.required:
                cls._raise(spec, [cls._required_violation()])
            return

        if any(v is None for v in value):
            cls._raise(spec, [cls._invalid_value_violation()])

        if any(not isinstance(v, spec.base_type) for v in value):
            cls._raise(spec, [cls._invalid_value_violation()])

        violations: List[FilterViolation] = []

        duplicates = set()
        seen = set()

        for endpoint in value:
            violations.extend(cls._validate_bounds(spec, endpoint))
            violations.extend(cls._validate_choices(spec, endpoint))

            if endpoint in seen:
                duplicates.add(endpoint)
            else:
                seen.add(endpoint)

        if duplicates:
            violations.append(cls._duplicate_violation(duplicates))

        if violations:
            cls._raise(spec, violations)

    @classmethod
    def _validate_json(cls, spec: FilterSpec, value: Optional[Any]) -> None:
        """The item schema is enforced by pydantic before this runs, so only
        presence and item count are checked here."""
        if value is None or (isinstance(value, (tuple, list)) and not value):
            if spec.required:
                cls._raise(spec, [cls._required_violation()])
            return

        if not isinstance(value, (tuple, list)):
            cls._raise(spec, [cls._invalid_value_violation()])

        violations = cls._validate_length(spec, value)

        if violations:
            cls._raise(spec, violations)

    # --- constraint checks ------------------------------------------------

    @classmethod
    def _validate_bounds(cls, spec: FilterSpec, value: Any) -> List[FilterViolation]:
        violations: List[FilterViolation] = []

        if spec.gt is not None and not value > spec.gt:
            violations.append(cls._bound_violation(spec, "gt"))
        if spec.gte is not None and not value >= spec.gte:
            violations.append(cls._bound_violation(spec, "gte"))
        if spec.lt is not None and not value < spec.lt:
            violations.append(cls._bound_violation(spec, "lt"))
        if spec.lte is not None and not value <= spec.lte:
            violations.append(cls._bound_violation(spec, "lte"))

        return violations

    @classmethod
    def _validate_length(cls, spec: FilterSpec, value: Any) -> List[FilterViolation]:
        if spec.min_length is None and spec.max_length is None:
            return []

        length = len(value)

        if (spec.min_length is not None and length < spec.min_length) or (
            spec.max_length is not None and length > spec.max_length
        ):
            return [cls._length_violation(spec)]

        return []

    @classmethod
    def _validate_choices(cls, spec: FilterSpec, value: Any) -> List[FilterViolation]:
        if spec.choices is None or value in spec.choices:
            return []

        return [cls._choices_violation(spec)]

    # --- violation builders -----------------------------------------------
    # `field` and `location` are deliberately absent: pydantic tags the error
    # with the field's `loc` on the way out, and the framework already knows
    # the model came from the query string.

    @staticmethod
    def _required_violation() -> FilterViolation:
        return FilterViolation(
            type=FilterErrorType.REQUIRED,
            message=REQUIRED_VALUE_MESSAGE,
            context={},
        )

    @staticmethod
    def _invalid_value_violation() -> FilterViolation:
        return FilterViolation(
            type=FilterErrorType.INVALID_VALUE,
            message=INVALID_VALUE_MESSAGE,
            context={},
        )

    @staticmethod
    def _bound_violation(spec: FilterSpec, bound: str) -> FilterViolation:
        return FilterViolation(
            type=FilterErrorType.BOUND,
            message=INVALID_VALUE_MESSAGE,
            context={"bounds": {bound: getattr(spec, bound)}},
        )

    @staticmethod
    def _range_order_violation(low: Any, high: Any) -> FilterViolation:
        return FilterViolation(
            type=FilterErrorType.RANGE_ORDER,
            message=INVALID_VALUE_MESSAGE,
            context={"bounds": {"low": low, "high": high}},
        )

    @staticmethod
    def _length_violation(spec: FilterSpec) -> FilterViolation:
        return FilterViolation(
            type=FilterErrorType.LENGTH,
            message=INVALID_VALUE_MESSAGE,
            context={
                "bounds": {
                    "min_length": spec.min_length,
                    "max_length": spec.max_length,
                }
            },
        )

    @staticmethod
    def _choices_violation(spec: FilterSpec) -> FilterViolation:
        return FilterViolation(
            type=FilterErrorType.CHOICES,
            message=INVALID_VALUE_MESSAGE,
            context={
                "values": [c.value if isinstance(c, Enum) else c for c in spec.choices]
            },
        )

    @staticmethod
    def _duplicate_violation(duplicates: Iterable[Any]) -> FilterViolation:
        return FilterViolation(
            type=FilterErrorType.DUPLICATED,
            message=DUPLICATED_VALUE_MESSAGE,
            context={"values": sorted(duplicates, key=repr)},
        )
