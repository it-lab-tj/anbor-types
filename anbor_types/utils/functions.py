from datetime import datetime
from enum import Enum
import re
from typing import Any, Tuple, Type

re_rm_whitespace = re.compile(r"\s+")


def parse_str(v: str) -> str:
    return re_rm_whitespace.sub(" ", v.strip())


def parse_single_line_str(v: str) -> str:
    return parse_str(v).replace("\n", "")


def min_length_exceeded(field: str) -> str:
    return f"Длина {field} слишком короткая"


def max_length_exceeded(field: str) -> str:
    return f"Превышена максимально допустимая длина {field}"


def check_timezone(v: datetime) -> datetime:
    if v.tzinfo is None:
        raise ValueError("datetime must include timezone information")
    return v


def tuple_from_enum(enm: Type[Enum]) -> Tuple[Any]:
    return tuple(enm.__members__.values())
