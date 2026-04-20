from typing import List, Optional
from anbor_types import Command
from anbor_types.storage.so.commands import ApplicationStockOperationsCommand


class SOGApplicationCommand(Command):
    stock_operations: List[ApplicationStockOperationsCommand]
    description: Optional[str] = None


class SOGConfirmCommand(Command):
    sog_id: int
