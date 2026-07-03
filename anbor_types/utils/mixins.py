from typing import Set, Optional, Self

from pydantic import model_validator

from anbor_types.api.ordering import OrderingContainer


class OrderingQueryMixin:
    ordering: Optional[OrderingContainer] = None

    _allowed_fields: Set[str]

    @model_validator(mode="after")
    def validate_ordering(self) -> Self:
        if self.ordering and self.ordering.items:
            given_fields = set(item.field for item in self.ordering.items)
            unexpected_fields = given_fields - self._allowed_fields

            if unexpected_fields:
                raise ValueError(
                    f"Unexpected fields for ordering: {', '.join(unexpected_fields)}"
                )

        return self

    @classmethod
    def get_allowed_fields(cls) -> Set[str]:
        return cls._allowed_fields if isinstance(cls._allowed_fields, set) else set()
