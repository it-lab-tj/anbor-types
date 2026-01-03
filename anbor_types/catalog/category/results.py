from anbor_types import ID_T, BasePydanticModel



class CategoryCreateResult(BasePydanticModel):
    id: ID_T
    name: str
