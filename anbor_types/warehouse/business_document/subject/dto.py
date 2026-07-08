from datetime import datetime
from decimal import Decimal
from typing import Optional, List

import msgspec
from pydantic import Field

from anbor_types import ID_T, BasePydanticModel
from anbor_types.common.dto import FileShortDTO
from anbor_types.handbook.region.dto import RegionShortDTO
from anbor_types.warehouse.constants.enums import SubjectKindEnum


class SubjectCreateDTO(BasePydanticModel):
    name: str
    kind: SubjectKindEnum
    full_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    itn: Optional[str] = None
    comment: Optional[str] = None
    index: Optional[int] = None
    region: Optional[ID_T] = None
    information: Optional[str] = None
    files: Optional[List[ID_T]] = Field(default=None)


class SubjectListDTO(msgspec.Struct):
    id: ID_T
    name: str
    balance: Decimal
    kind: SubjectKindEnum
    created_at: datetime
    status: int
    full_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    region: Optional[RegionShortDTO] = None


class SubjectCreateResultDTO(SubjectListDTO): ...


class SubjectDetailedDTO(msgspec.Struct):
    id: ID_T
    name: str
    balance: Decimal
    kind: SubjectKindEnum
    created_at: datetime
    updated_at: datetime
    status: int
    full_name: Optional[str] = None
    itn: Optional[str] = None
    address: Optional[str] = None
    comment: Optional[str] = None
    information: Optional[str] = None
    index: Optional[int] = None
    files: Optional[List[FileShortDTO]] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    region: Optional[RegionShortDTO] = None


class SubjectUpdateDTO(BasePydanticModel):
    name: str
    full_name: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    itn: Optional[str] = None
    comment: Optional[str] = None
    index: Optional[int] = None
    region: Optional[ID_T] = None
    information: Optional[str] = None
    files: Optional[List[ID_T]] = Field(default=None)


class SubjectForBusinessDocumentShortDataDTO(msgspec.Struct):
    id: ID_T
    name: str
    balance: Decimal
    kind: SubjectKindEnum


class SubjectShortDTO(msgspec.Struct):
    id: ID_T
    name: str


class SubjectBalanceDTO(msgspec.Struct):
    id: ID_T
    balance: Decimal


class SubjectStockProductsDTO(msgspec.Struct):
    class Characteristics(msgspec.Struct):
        characteristic_id: ID_T
        characteristic: str
        value_id: ID_T
        value: str

    product_id: ID_T
    name: str
    remains: Decimal
    image_url: str
    measurement_unit: str
    slug: str
