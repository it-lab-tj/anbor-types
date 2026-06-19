from anbor_types import ID_T, Command
from anbor_types.wallet.wallet_document.dto import (
    WalletDocumentCreateDTO,
    WalletDocumentUpdateDTO,
)


class WalletDocumentCreateCommand(WalletDocumentCreateDTO, Command): ...


class WalletDocumentUpdateCommand(WalletDocumentUpdateDTO, Command):
    id: ID_T

class WalletDocumentDeleteCommand(Command):
    id: ID_T