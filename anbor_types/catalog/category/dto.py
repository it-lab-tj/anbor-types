from anbor_types import ID_T, BasePydanticModel


class CharValueDTO(BasePydanticModel):
    characteristic_id: ID_T
    value_id: ID_T
