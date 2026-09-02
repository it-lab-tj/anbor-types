from decimal import Decimal

import msgspec

from anbor_types.identity.user.dto import StaffMemberShortDTO


class StaffBusinessDocumentSummaryDTO(msgspec.Struct):
    """Commission base for one staff member.

    ``total_amount`` is the sum of the documents they authored, in base
    currency; ``percentage_amount`` is the requested share of it.
    """

    user: StaffMemberShortDTO
    total_amount: Decimal
    percentage_amount: Decimal
