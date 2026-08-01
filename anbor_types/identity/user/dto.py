from datetime import datetime
from typing import List, Optional

import msgspec
from pydantic import Field

from anbor_types import ID_T, BasePydanticModel
from anbor_types.common.dto import FileShortDTO, NameIdDTO


class AuthorInfoShortDTO(msgspec.Struct):
    id: ID_T
    full_name: str


class StaffMemberShortDTO(msgspec.Struct):
    id: ID_T
    full_name: str


# --------------------------------------------------------------------------- #
# Staff member CRUD
#
# `Staff` is only a *kind* of user (`role == STAFF`); these DTOs describe the
# staff-management surface. Input DTOs stay plain (validation lives in the
# app-layer validators); read DTOs are msgspec.Struct for fast serialization.
# --------------------------------------------------------------------------- #


class StaffMemberCreateDTO(BasePydanticModel):
    username: str
    email: str
    first_name: str
    last_name: str
    # Phone is required by the domain user-creation validation profile.
    phone: str
    information: Optional[str] = None
    address: Optional[str] = None
    description: Optional[str] = None
    avatar_id: Optional[ID_T] = None
    job_position_id: Optional[ID_T] = None
    files: Optional[List[ID_T]] = Field(default=None)


class StaffMemberUpdateDTO(BasePydanticModel):
    email: str
    first_name: str
    last_name: str
    phone: str
    information: Optional[str] = None
    address: Optional[str] = None
    description: Optional[str] = None
    avatar_id: Optional[ID_T] = None
    job_position_id: Optional[ID_T] = None
    files: Optional[List[ID_T]] = Field(default=None)


class StaffMemberCreateResultDTO(msgspec.Struct):
    id: ID_T
    username: str
    email: str
    full_name: str


class StaffMemberListDTO(msgspec.Struct):
    id: ID_T
    username: str
    status: int
    created_at: datetime
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    avatar_url: Optional[str] = None
    job_position: Optional[NameIdDTO] = None


class StaffMemberDetailedDTO(msgspec.Struct):
    id: ID_T
    username: str
    status: int
    created_at: datetime
    updated_at: datetime
    email_confirmed: bool
    phone_confirmed: bool
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    full_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    information: Optional[str] = None
    address: Optional[str] = None
    description: Optional[str] = None
    avatar_url: Optional[str] = None
    company: Optional[NameIdDTO] = None
    job_position: Optional[NameIdDTO] = None
    files: Optional[List[FileShortDTO]] = None
