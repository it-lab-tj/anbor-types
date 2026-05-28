from datetime import datetime
from decimal import Decimal
from typing import Optional, List

import msgspec
from anbor_types import ID_T, BasePydanticModel
from anbor_types.handbook.region.dto import RegionShortDTO
from anbor_types.warehouse.constants.enums import SubjectKindEnum


class SubjectCreateDTO(BasePydanticModel):
    name: str
    kind: SubjectKindEnum
    fullname: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None
    itn: Optional[str] = None
    comment: Optional[str] = None
    index: Optional[int] = None
    region: Optional[ID_T] = None
    information: Optional[str] = None
    files: Optional[List[ID_T]] = None


class SubjectListsDTO(msgspec.Struct):
    id: ID_T
    name: str
    balance: Decimal
    kind: SubjectKindEnum
    created_at: datetime
    fullname: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    region: Optional[RegionShortDTO] = None
