from typing import Literal


from anbor_types import ID_T, Command
from anbor_types.wallet.constants import WalletDocumentKindEnum
from anbor_types.wallet.wallet_document.dto import (
    WalletDocumentCreateDTO,
    WalletDocumentTransferCreateDTO,
    WalletDocumentUpdateDTO,
)


class WalletDocumentCreateCommand(WalletDocumentCreateDTO, Command):
    kind: Literal[WalletDocumentKindEnum.INCOME, WalletDocumentKindEnum.EXPENSE]


class WalletDocumentTransferCreateCommand(WalletDocumentTransferCreateDTO, Command): ...


class WalletDocumentUpdateCommand(WalletDocumentUpdateDTO, Command):
    id: ID_T


class WalletDocumentDeleteCommand(Command):
    id: ID_T
