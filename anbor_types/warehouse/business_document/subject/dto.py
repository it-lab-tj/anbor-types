from datetime import datetime
from decimal import Decimal
from typing import Optional, List

import msgspec
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
    files: Optional[List[ID_T]] = None


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
    files: Optional[List[ID_T]] = None


class SubjectForBusinessDocumentShortDataDTO(msgspec.Struct):
    id: ID_T
    name: str
    balance: Decimal
    kind: SubjectKindEnum
