from decimal import Decimal
from typing import List, Optional

import msgspec

from anbor_types import ID_T
from anbor_types.catalog.category.dto import (
    CategoryCharacteristicDTO,
    CharacteristicValuePairDTO,
)
from anbor_types.common.dto import NameIdDTO


class CatalogFeedImageDTO(msgspec.Struct):
    """An absolute URL, unlike ``ProductDetailedListImageDTO``'s stored path.

    The consumer fetches the bytes and keeps them under its own storage key, so
    this URL is something it uses once and does not persist. Handing it a
    media-root-relative path instead would make it reconstruct the `/media/`
    prefix from a convention nothing in the payload states.
    """

    id: ID_T
    name: str
    url: str


class CatalogFeedVariantDTO(msgspec.Struct):
    """One sellable variant of the product.

    ``id`` is the variant row's id, not the content-addressed characteristic
    tuple it points at: the tuple is shared between products, the row is not.
    ``char_values`` is empty for a product that has no characteristics.
    """

    id: ID_T
    identifier: str
    char_values: List[CharacteristicValuePairDTO]


class CatalogFeedCategoryDTO(msgspec.Struct):
    """The product's category as it stood at the product's last change.

    Categories are not tracked on their own, so a category renamed without any
    of its products being touched does not reach the consumer until one of them
    changes. Deliberate -- see the feed contract.
    """

    id: ID_T
    name: str
    parent_id: Optional[ID_T]
    characteristics: List[CategoryCharacteristicDTO]


class CatalogFeedItemDTO(msgspec.Struct):
    """One self-contained product. The consumer never needs a second request to
    describe it: its category, that category's characteristics and values, its
    images and its variants all travel with it.

    Carries no stock: `remains` lives on `handbook_product` and moves with every
    sale, receipt and transfer, which would turn the feed into a warehouse
    traffic log instead of a record of catalog edits.
    """

    id: ID_T
    name: str
    slug: str
    vendor_code: Optional[str]
    description: Optional[str]
    information: Optional[str]
    selling_price: Decimal
    measurement_unit: NameIdDTO
    category: CatalogFeedCategoryDTO
    images: List[CatalogFeedImageDTO]
    variants: List[CatalogFeedVariantDTO]

    # A string, not a number: `xid8` is an unsigned 64-bit transaction id and a
    # JSON number loses precision above 2**53. The consumer compares it as an
    # integer and stores it as a `source_xid`, so the text form has to round-trip
    # exactly.
    change_xid: str


class CatalogFeedPageDTO(msgspec.Struct):
    """One page of the feed.

    ``next_cursor`` is where the next request resumes, and it advances only past
    rows this page actually served: a transaction still in flight holds the
    cursor back rather than letting its rows fall behind it.
    """

    items: List[CatalogFeedItemDTO]
    next_cursor: str
    has_more: bool
