from anbor_types import ID_T, BasePydanticModel


class ProductCreateResult(BasePydanticModel):
    """Result after product creation"""

    id: ID_T