from typing import Set, Optional, Self

from pydantic import model_validator

from anbor_types.api.ordering import OrderingContainer


class OrderingQueryMixin:
    ordering: Optional[OrderingContainer] = None

    _ordering_allowed_fields: Set[str]

    @model_validator(mode="after")
    def validate_ordering(self) -> Self:
        if self.ordering and self.ordering.items:
            given_fields = set(item.field for item in self.ordering.items)
            unexpected_fields = given_fields - self._ordering_allowed_fields

            if unexpected_fields:
                raise ValueError(
                    f"Unexpected fields for ordering: {', '.join(unexpected_fields)}"
                )

        return self

    @classmethod
    def get_allowed_fields(cls) -> Set[str]:
        """The sortable field names, readable off the class.

        Accessed on an *instance* pydantic resolves a private attribute to its
        value, but on the class it hands back the `ModelPrivateAttr`
        descriptor -- so the plain isinstance check returned an empty set for
        every query. That made the OpenAPI `Allowed fields` list render empty
        on every ordering parameter. Unwrap the descriptor's default.
        """
        allowed = cls._ordering_allowed_fields

        if isinstance(allowed, set):
            return allowed

        default = getattr(allowed, "default", None)

        return default if isinstance(default, set) else set()
