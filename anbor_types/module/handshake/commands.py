from anbor_types import Command
from anbor_types.module.handshake.dto import HandshakeConfirmationDTO


class HandshakeConfirmationCommand(HandshakeConfirmationDTO, Command):
    signature: str  # base64 encoded string
