# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BenefitPlanTypeEnum(str, enum.Enum):
    """
    - `MEDICAL` - MEDICAL
    - `HEALTH_SAVINGS` - HEALTH_SAVINGS
    - `INSURANCE` - INSURANCE
    - `RETIREMENT` - RETIREMENT
    - `OTHER` - OTHER
    """

    MEDICAL = "MEDICAL"
    HEALTH_SAVINGS = "HEALTH_SAVINGS"
    INSURANCE = "INSURANCE"
    RETIREMENT = "RETIREMENT"
    OTHER = "OTHER"

    def visit(
        self,
        medical: typing.Callable[[], T_Result],
        health_savings: typing.Callable[[], T_Result],
        insurance: typing.Callable[[], T_Result],
        retirement: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BenefitPlanTypeEnum.MEDICAL:
            return medical()
        if self is BenefitPlanTypeEnum.HEALTH_SAVINGS:
            return health_savings()
        if self is BenefitPlanTypeEnum.INSURANCE:
            return insurance()
        if self is BenefitPlanTypeEnum.RETIREMENT:
            return retirement()
        if self is BenefitPlanTypeEnum.OTHER:
            return other()
