import base64

from pydantic import field_validator

from anbor_types import ID_T, Command
from anbor_types.catalog.annotated import ATFileName


class FileUploadCommand(Command):
    name: ATFileName
    file: memoryview

    @field_validator("file", mode="before")
    @classmethod
    def convert_file(cls, v: str) -> memoryview:
        if not v:
            raise ValueError("file is required")
        try:
            return memoryview(base64.b64decode(v))
        except Exception:
            raise ValueError("Invalid Data format")


class FileDeleteCommand(Command):
    id: ID_T
