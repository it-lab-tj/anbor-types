from typing import List

import msgspec
from pydantic import Field
from anbor_types import ID_T, BasePydanticModel
from anbor_types.identity.company.customer_display import (
    DEFAULT_ACCENT_COLOR,
    ACCENT_COLOR_PATTERN,
    QR_URL_PATTERN,
    SLIDE_SECONDS_MAX,
    DEFAULT_SLIDE_SECONDS,
    SLIDE_SECONDS_MIN,
    SLIDES_MAX,
    SOCIAL_LINKS_MAX,
    CustomerDisplaySlideInputDTO,
    CustomerDisplaySocialLinkInputDTO,
)


class CompanyListDTO(msgspec.Struct):
    id: ID_T
    name: str
    nick: str
    phone_number: str
    email: str


class CompanyShortListDTO(msgspec.Struct):
    id: ID_T
    name: str


class CustomerDisplaySettingsUpdateDTO(BasePydanticModel):
    """Full-state replace: the settings screen submits what it shows, and
    anything absent is reset to its default. Same shape as the read DTO minus
    the resolved image URLs and the `updated_*` stamp."""

    welcome_title: str = Field(default="", max_length=100)
    welcome_subtitle: str = Field(default="", max_length=200)
    thank_you_title: str = Field(default="", max_length=100)
    ticker_text: str = Field(default="", max_length=300)

    accent_color: str = Field(
        default=DEFAULT_ACCENT_COLOR,
        pattern=ACCENT_COLOR_PATTERN,
    )

    slide_seconds: int = Field(
        default=DEFAULT_SLIDE_SECONDS,
        ge=SLIDE_SECONDS_MIN,
        le=SLIDE_SECONDS_MAX,
    )

    show_promo_during_sale: bool = False

    qr_url: str = Field(
        default="",
        max_length=2000,
        pattern=QR_URL_PATTERN,
    )
    qr_caption: str = Field(default="", max_length=100)

    slides: List[CustomerDisplaySlideInputDTO] = Field(
        default_factory=list,
        max_length=SLIDES_MAX,
    )

    social_links: List[CustomerDisplaySocialLinkInputDTO] = Field(
        default_factory=list,
        max_length=SOCIAL_LINKS_MAX,
    )
