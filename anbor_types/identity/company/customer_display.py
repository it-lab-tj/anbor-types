"""The customer display: the second screen a cashier turns towards the buyer.

Only its *look* lives on the server -- titles, ticker, accent colour, slides,
QR code and social links -- one record per company. The receipt itself (lines,
totals, status) travels from the cashier's window to the display window over
``BroadcastChannel`` in the same browser and never reaches the backend.
"""

from datetime import datetime
from enum import StrEnum
from typing import List, Optional

import msgspec
from pydantic import Field

from anbor_types import ID_T, BasePydanticModel, Command, Query
from anbor_types.common.dto import NameIdDTO

ACCENT_COLOR_PATTERN = r"^#[0-9a-fA-F]{6}$"
# Empty means "no QR code".
QR_URL_PATTERN = r"^(https?://\S+)?$"

DEFAULT_ACCENT_COLOR = "#2fa8ff"
DEFAULT_SLIDE_SECONDS = 8
SLIDE_SECONDS_MIN = 3
SLIDE_SECONDS_MAX = 60
SLIDES_MAX = 20
SOCIAL_LINKS_MAX = 10


class SocialNetworkEnum(StrEnum):
    INSTAGRAM = "instagram"
    WHATSAPP = "whatsapp"
    TELEGRAM = "telegram"
    FACEBOOK = "facebook"
    TIKTOK = "tiktok"
    YOUTUBE = "youtube"
    WEBSITE = "website"


# ------------------------------------------------------------------ #
# Read side
# ------------------------------------------------------------------ #


class CustomerDisplaySlideDTO(msgspec.Struct):
    """`medium` / `original` are full URLs resolved from the gallery at read
    time, so a recropped image shows up without re-saving the settings."""

    image_id: ID_T
    caption: str
    position: int
    medium: Optional[str] = None
    original: Optional[str] = None


class CustomerDisplaySocialLinkDTO(msgspec.Struct):
    network: SocialNetworkEnum
    handle: str
    position: int


class CustomerDisplaySettingsDTO(msgspec.Struct):
    """`updated_at` / `updated_by` are null until the settings are saved for
    the first time -- until then every field is its default."""

    welcome_title: str = ""
    welcome_subtitle: str = ""
    thank_you_title: str = ""
    ticker_text: str = ""
    accent_color: str = DEFAULT_ACCENT_COLOR
    slide_seconds: int = DEFAULT_SLIDE_SECONDS
    show_promo_during_sale: bool = False
    qr_url: str = ""
    qr_caption: str = ""
    slides: List[CustomerDisplaySlideDTO] = msgspec.field(default_factory=list)
    social_links: List[CustomerDisplaySocialLinkDTO] = msgspec.field(
        default_factory=list
    )
    updated_at: Optional[datetime] = None
    updated_by: Optional[NameIdDTO] = None


# ------------------------------------------------------------------ #
# Write side
# ------------------------------------------------------------------ #


class CustomerDisplaySlideInputDTO(BasePydanticModel):
    image_id: ID_T
    caption: str = Field(default="", max_length=150)
    position: int = Field(ge=0, lt=SLIDES_MAX)


class CustomerDisplaySocialLinkInputDTO(BasePydanticModel):
    network: SocialNetworkEnum
    handle: str = Field(min_length=1, max_length=150)
    position: int = Field(ge=0, lt=SOCIAL_LINKS_MAX)


class CustomerDisplaySettingsUpdateCommand(Command):
    """Full-state replace: the settings screen submits what it shows, and
    anything absent is reset to its default. Same shape as the read DTO minus
    the resolved image URLs and the `updated_*` stamp."""

    welcome_title: str = Field(default="", max_length=100)
    welcome_subtitle: str = Field(default="", max_length=200)
    thank_you_title: str = Field(default="", max_length=100)
    ticker_text: str = Field(default="", max_length=300)
    accent_color: str = Field(
        default=DEFAULT_ACCENT_COLOR, pattern=ACCENT_COLOR_PATTERN
    )
    slide_seconds: int = Field(
        default=DEFAULT_SLIDE_SECONDS, ge=SLIDE_SECONDS_MIN, le=SLIDE_SECONDS_MAX
    )
    show_promo_during_sale: bool = False
    qr_url: str = Field(default="", max_length=2000, pattern=QR_URL_PATTERN)
    qr_caption: str = Field(default="", max_length=100)
    slides: List[CustomerDisplaySlideInputDTO] = Field(
        default_factory=list, max_length=SLIDES_MAX
    )
    social_links: List[CustomerDisplaySocialLinkInputDTO] = Field(
        default_factory=list, max_length=SOCIAL_LINKS_MAX
    )


class CustomerDisplaySettingsQuery(Query): ...
