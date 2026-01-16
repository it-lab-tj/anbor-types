from typing import List
from anbor_types import Command
from anbor_types.storage.so.commands import ApplicationStockOperationsCommand


class SOGApplicationCommand(Command):
    stock_operations: List[ApplicationStockOperationsCommand]
