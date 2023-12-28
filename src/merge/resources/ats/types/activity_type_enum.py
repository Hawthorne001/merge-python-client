# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ActivityTypeEnum(str, enum.Enum):
    """
    - `NOTE` - NOTE
    - `EMAIL` - EMAIL
    - `OTHER` - OTHER
    """

    NOTE = "NOTE"
    EMAIL = "EMAIL"
    OTHER = "OTHER"

    def visit(
        self,
        note: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ActivityTypeEnum.NOTE:
            return note()
        if self is ActivityTypeEnum.EMAIL:
            return email()
        if self is ActivityTypeEnum.OTHER:
            return other()
