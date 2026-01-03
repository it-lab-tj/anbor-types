import re
from datetime import UTC, datetime


re_rm_whitespace = re.compile(r"\s+")


def parse_str(v: str) -> str:
    return re_rm_whitespace.sub(" ", v.strip())


def parse_single_line_str(v: str) -> str:
    return parse_str(v).replace("\n", "")


def min_length_exceeded(field: str) -> str:
    return f"Длина {field} слишком короткая"


def max_length_exceeded(field: str) -> str:
    return f"Превышена максимально допустимая длина {field}"
