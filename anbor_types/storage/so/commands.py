from decimal import Decimal
from typing import List
from anbor_types import Command
from anbor_types.catalog.category.dto import CharValuePairDTO


class ApplicationStockOperationsCommand(Command):
    product: int
    count: Decimal
    price: Decimal
    discount: Decimal
    characteristics: List[CharValuePairDTO]
