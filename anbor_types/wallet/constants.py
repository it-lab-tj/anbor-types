from decimal import Decimal
from enum import IntEnum
from typing import Optional


class WalletDocumentKindEnum(IntEnum):
    """What a money document is.

    EXPENSE and INCOME are a DIRECTION, and the direction is carried by the
    sign of `amount`, so they are never stored -- a stored `kind` of NULL means
    "an ordinary movement, read the sign". They remain part of the API in both
    directions: clients send them, clients receive them.

    Every other member IS stored, because it is not something a sign can say.
    """

    EXPENSE = 0
    INCOME = 1
    TRANSFER = 2
    CASH_DESK_RECALCULATE = 3

    @classmethod
    def project(
        cls, stored_kind: Optional[int], amount: Decimal
    ) -> "WalletDocumentKindEnum":
        """The kind as the API speaks it, from what the database holds.

        A stored kind wins. Otherwise the sign decides, and it always can:
        a document with no stored kind may not have a zero amount (enforced by
        `chk__wallet_document__kind_or_signed_amount`).
        """
        if stored_kind is not None:
            return cls(stored_kind)

        return cls.EXPENSE if amount < 0 else cls.INCOME

    @classmethod
    def to_stored(
        cls, kind: "WalletDocumentKindEnum"
    ) -> Optional["WalletDocumentKindEnum"]:
        """What to put in the `kind` column -- None for a plain direction."""
        if kind not in (cls.EXPENSE, cls.INCOME):
            return None

        return kind

    @classmethod
    def to_signed_amount(
        cls, kind: "WalletDocumentKindEnum", amount: Decimal
    ) -> Decimal:
        """Turn a client's (kind, positive amount) into the stored signed one.

        Only EXPENSE flips: it drains the cash desk. Every other kind already
        means what its own sign says -- a recalculation delta is signed by the
        caller, and a transfer's direction is its two desk ids.
        """
        if kind == cls.EXPENSE:
            return -abs(amount)

        if kind == cls.INCOME:
            return abs(amount)

        return amount

    @classmethod
    def to_client_amount(
        cls, kind: "WalletDocumentKindEnum", amount: Decimal
    ) -> Decimal:
        """The stored signed amount as the API has always presented it.

        EXPENSE and INCOME go back out POSITIVE, exactly as legacy sent them --
        the direction is the `kind` field, and a client that has always drawn
        "500" for an expense keeps drawing "500".

        A CASH_DESK_RECALCULATE keeps its sign: it is a correction, its whole
        content is the signed delta, and there is no legacy behaviour to match
        because legacy had no such document.
        """
        if kind in (cls.EXPENSE, cls.INCOME):
            return abs(amount)

        return amount
