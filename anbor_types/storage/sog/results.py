import msgspec


class SOGApplicationCreationResult(msgspec.Struct):
    sog_id: int


class SOGConfirmationResult(msgspec.Struct):
    sog_id: int
