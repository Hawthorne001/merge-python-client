# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .group_type import GroupType
from .remote_data import RemoteData

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Group(pydantic.BaseModel):
    """
    # The Group Object

    ### Description

    The `Group` object is used to represent any subset of employees across, for example, `DEPARTMENT` or `TEAM`. Employees can be in multiple Groups.

    ### Usage Example

    Fetch from the `LIST Employee` endpoint and expand groups to view an employee's groups.
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    created_at: typing.Optional[dt.datetime]
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    parent_group: typing.Optional[str] = pydantic.Field(description="The parent group for this group.")
    name: typing.Optional[str] = pydantic.Field(description="The group name.")
    type: typing.Optional[GroupType] = pydantic.Field(
        description=(
            "The Group type returned directly from the third-party.\n"
            "\n"
            "- `TEAM` - TEAM\n"
            "- `DEPARTMENT` - DEPARTMENT\n"
            "- `COST_CENTER` - COST_CENTER\n"
            "- `BUSINESS_UNIT` - BUSINESS_UNIT\n"
            "- `GROUP` - GROUP\n"
        )
    )
    remote_was_deleted: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether or not this object has been deleted in the third party platform."
    )
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        json_encoders = {dt.datetime: serialize_datetime}
