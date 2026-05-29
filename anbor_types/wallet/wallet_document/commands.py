from anbor_types import Command
from anbor_types.wallet.wallet_document.dto import (
    WalletDocumentCreateDTO,
    WalletDocumentUpdateDTO,
)


class WalletDocumentCreateCommand(WalletDocumentCreateDTO, Command): ...


class WalletDocumentUpdateCommand(WalletDocumentUpdateDTO, Command): ...
