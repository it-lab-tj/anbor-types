from anbor_types import Command
from anbor_types.wallet.wallet_document.dto import (
    WalletDocumentCreateDTO,
    WalletDocumentUpdateDTO,
)
from src.app.shared_kernel.types.base_types import ID_T


class WalletDocumentCreateCommand(WalletDocumentCreateDTO, Command): ...


class WalletDocumentUpdateCommand(WalletDocumentUpdateDTO, Command):
    id: ID_T
