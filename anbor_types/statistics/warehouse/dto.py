from datetime import date

import msgspec
from decimal import Decimal
from typing import List


class InventoryAnalyticsOverviewDTO(msgspec.Struct):
    products_count: Decimal
    created_product_count: Decimal
    warehouse_stock_cost: Decimal
    deficit_count: Decimal
    frozen_capital: Decimal


class StockByCategoryDTO(msgspec.Struct):
    category_name: str
    total_cost: Decimal


class InventoryAnalyticsCategoryFlowDTO(msgspec.Struct):
    stock_by_category: List[StockByCategoryDTO]


class InventoryAnalyticsLiquidDTO(msgspec.Struct):
    product_name: str
    last_sold_at: date


class InventoryAnalyticsIlliquidDTO(msgspec.Struct):
    product_name: str
    last_sold_at: date


class InventoryAnalyticsCashFlowDTO(msgspec.Struct):
    income: Decimal
    expense: Decimal
