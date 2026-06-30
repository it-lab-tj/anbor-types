from datetime import date

import msgspec
from decimal import Decimal
from typing import List


class WarehouseInventoryOverviewDTO(msgspec.Struct):
    products_count: Decimal
    created_product_count: Decimal
    warehouse_stock_cost: Decimal
    deficit_count: Decimal
    frozen_capital: Decimal


class StockByCategoryDTO(msgspec.Struct):
    category_name: str
    total_cost: Decimal


class WarehouseInventoryCategoryFlowDTO(msgspec.Struct):
    stock_by_category: List[StockByCategoryDTO]
    income_total: Decimal
    expense_total: Decimal


class WarehouseInventoryTopSellingDTO(msgspec.Struct):
    product_name: str
    last_saled: date
