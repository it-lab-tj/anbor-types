from anbor_types import Command
from anbor_types.module.handshake.dto import HandshakeConfirmationDTO


class HandshakeConfirmationCommand(HandshakeConfirmationDTO, Command):
    """`source_ip` is resolved from the connection by the route and is the only
    thing that decides which handshake a confirmation may consume.

    It is deliberately not part of `HandshakeConfirmationDTO`, which is the
    request body: the route builds this command field by field, so nothing a
    caller writes can reach it. A hostname or an address in the body would be
    the caller's own claim about itself.
    """

    source_ip: str
