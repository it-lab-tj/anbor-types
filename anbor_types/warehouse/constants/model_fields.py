from enum import auto

from src.app.shared_kernel.constants.enums import ModelFieldsBaseEnum


class BusinessDocumentField(ModelFieldsBaseEnum):
    ID = auto()
    DEBIT = auto()
    CREDIT = auto()
    STORAGE = auto()
    CURRENCY = auto()
    RATE = auto()
    PAID = auto()
    SHIPPED_AT = auto()
    CONFIRMED_AT = auto()
    ITEMS = auto()
    CREATED_AT = auto()
    UPDATED_AT = auto()
    CREATED_BY = auto()
    UPDATED_BY = auto()


class BusinessDocumentItemField(ModelFieldsBaseEnum):
    ID = auto()
    ENTRY = auto()
    PRICE = auto()
    COUNT = auto()
    CREATED_BY = auto()
    CREATED_AT = auto()
    UPDATED_AT = auto()
