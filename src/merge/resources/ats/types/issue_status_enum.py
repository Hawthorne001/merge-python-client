# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class IssueStatusEnum(str, enum.Enum):
    """
    - `ONGOING` - ONGOING
    - `RESOLVED` - RESOLVED
    """

    ONGOING = "ONGOING"
    RESOLVED = "RESOLVED"

    def visit(self, ongoing: typing.Callable[[], T_Result], resolved: typing.Callable[[], T_Result]) -> T_Result:
        if self is IssueStatusEnum.ONGOING:
            return ongoing()
        if self is IssueStatusEnum.RESOLVED:
            return resolved()
