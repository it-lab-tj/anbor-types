from datetime import datetime
from decimal import Decimal
from typing import Optional, List

import msgspec
from pydantic import Field

from anbor_types import ID_T, BasePydanticModel
from anbor_types.api.constants import PRICE_MAX
from anbor_types.catalog.catalog_entry.dto import CatalogEntryImageListDTO
from anbor_types.common.dto import FileShortDTO
from anbor_types.handbook.region.dto import RegionShortDTO
from anbor_types.identity.user.dto import AuthorInfoShortDTO
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
    """A subject plus the role it plays. Use `NameIdDTO` when the kind is
    already implied by the field it sits on."""

    id: ID_T
    name: str
    kind: SubjectKindEnum


class SubjectBalanceDTO(msgspec.Struct):
    id: ID_T
    balance: Decimal


class SubjectRebalanceDTO(BasePydanticModel):
    """Set a subject balance to an absolute target.

    The client sends the new desired balance (`target_balance`); the backend
    computes the signed delta, records an immutable rebalance-history row, and
    writes a single WalletOperation for the delta. No WalletDocument is created.
    """

    target_balance: Decimal = Field(lt=Decimal(PRICE_MAX))
    operating_expense_id: ID_T
    comment: str
    files_ids: List[ID_T] = Field(default_factory=list)


class SubjectStockProductsDTO(msgspec.Struct):
    class Characteristics(msgspec.Struct):
        characteristic_id: ID_T
        characteristic: str
        value_id: ID_T
        value: str

    product_id: ID_T
    # None when the stocked lots carry no variant.
    variant_id: Optional[ID_T]
    name: str
    remains: Decimal
    measurement_unit: str
    slug: str
    status: int
    # Aggregated cost price of the product in this warehouse: sum(price * remains).
    cost_price: Decimal
    # Last confirmed sale date of the product (across the company). None if never sold.
    last_sold_date: Optional[datetime] = None
    images: List[CatalogEntryImageListDTO] = msgspec.field(default_factory=list)
    # The variant's characteristics, resolved to names. Empty when the lots
    # carry no variant. Same data as `CharacteristicValuePairDTO` under the
    # shorter field names this DTO shipped with.
    characteristics: List[Characteristics] = msgspec.field(default_factory=list)


class SubjectRebalanceResultDTO(msgspec.Struct):
    subject_id: ID_T
    previous_balance: Decimal
    new_balance: Decimal


class SubjectRebalanceHistoryListDTO(msgspec.Struct):
    """Row of the immutable rebalance history. Field names follow the model;
    `diff` is `new_balance - previous_balance` (None on the very first
    rebalance, where no previous balance was recorded)."""

    id: ID_T
    new_balance: Decimal
    created_at: datetime
    previous_balance: Optional[Decimal] = None
    diff: Optional[Decimal] = None
    created_by: Optional[AuthorInfoShortDTO] = None
