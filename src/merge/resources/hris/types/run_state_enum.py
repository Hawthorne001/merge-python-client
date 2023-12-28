# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class RunStateEnum(str, enum.Enum):
    """
    - `PAID` - PAID
    - `DRAFT` - DRAFT
    - `APPROVED` - APPROVED
    - `FAILED` - FAILED
    - `CLOSED` - CLOSED
    """

    PAID = "PAID"
    DRAFT = "DRAFT"
    APPROVED = "APPROVED"
    FAILED = "FAILED"
    CLOSED = "CLOSED"

    def visit(
        self,
        paid: typing.Callable[[], T_Result],
        draft: typing.Callable[[], T_Result],
        approved: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        closed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunStateEnum.PAID:
            return paid()
        if self is RunStateEnum.DRAFT:
            return draft()
        if self is RunStateEnum.APPROVED:
            return approved()
        if self is RunStateEnum.FAILED:
            return failed()
        if self is RunStateEnum.CLOSED:
            return closed()
