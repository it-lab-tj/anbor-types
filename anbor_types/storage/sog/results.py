import msgspec


class ApplicationSOGRequestResult(msgspec.Struct):
    sog_id: int


class ConfirmSOGRequestResult(msgspec.Struct):
    sog_id: int
