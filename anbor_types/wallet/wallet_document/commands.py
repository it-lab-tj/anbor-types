from anbor_types import Command
from anbor_types.wallet.wallet_document.dto import WalletDocumentCreateDTO


class WalletDocumentCreateCommand(WalletDocumentCreateDTO, Command): ...
