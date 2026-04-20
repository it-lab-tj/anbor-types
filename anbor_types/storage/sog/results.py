import msgspec


class SOGApplicationCreationResult(msgspec.Struct):
    sog_id: int
    vendor_code: str


class SOGConfirmationResult(msgspec.Struct):
    sog_id: int
    vendor_code: str
