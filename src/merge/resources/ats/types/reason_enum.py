# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ReasonEnum(str, enum.Enum):
    """
    - `GENERAL_CUSTOMER_REQUEST` - GENERAL_CUSTOMER_REQUEST
    - `GDPR` - GDPR
    - `OTHER` - OTHER
    """

    GENERAL_CUSTOMER_REQUEST = "GENERAL_CUSTOMER_REQUEST"
    GDPR = "GDPR"
    OTHER = "OTHER"

    def visit(
        self,
        general_customer_request: typing.Callable[[], T_Result],
        gdpr: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReasonEnum.GENERAL_CUSTOMER_REQUEST:
            return general_customer_request()
        if self is ReasonEnum.GDPR:
            return gdpr()
        if self is ReasonEnum.OTHER:
            return other()
