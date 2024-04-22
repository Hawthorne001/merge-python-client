# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .engagement_account import EngagementAccount
from .engagement_contacts_item import EngagementContactsItem
from .engagement_direction import EngagementDirection
from .engagement_engagement_type import EngagementEngagementType
from .engagement_owner import EngagementOwner
from .remote_data import RemoteData
from .remote_field import RemoteField

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class Engagement(pydantic.BaseModel):
    """
    # The Engagement Object

    ### Description

    The `Engagement` object is used to represent an interaction noted in a CRM system.

    ### Usage Example

    TODO
    """

    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    created_at: typing.Optional[dt.datetime]
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )
    owner: typing.Optional[EngagementOwner] = pydantic.Field(description="The engagement's owner.")
    content: typing.Optional[str] = pydantic.Field(description="The engagement's content.")
    subject: typing.Optional[str] = pydantic.Field(description="The engagement's subject.")
    direction: typing.Optional[EngagementDirection] = pydantic.Field(
        description=("The engagement's direction.\n" "\n" "- `INBOUND` - INBOUND\n" "- `OUTBOUND` - OUTBOUND\n")
    )
    engagement_type: typing.Optional[EngagementEngagementType] = pydantic.Field(
        description="The engagement type of the engagement."
    )
    start_time: typing.Optional[dt.datetime] = pydantic.Field(description="The time at which the engagement started.")
    end_time: typing.Optional[dt.datetime] = pydantic.Field(description="The time at which the engagement ended.")
    account: typing.Optional[EngagementAccount] = pydantic.Field(description="The account of the engagement.")
    contacts: typing.Optional[typing.List[typing.Optional[EngagementContactsItem]]]
    remote_was_deleted: typing.Optional[bool] = pydantic.Field(
        description="Indicates whether or not this object has been deleted in the third party platform."
    )
    field_mappings: typing.Optional[typing.Dict[str, typing.Any]]
    remote_data: typing.Optional[typing.List[RemoteData]]
    remote_fields: typing.Optional[typing.List[RemoteField]]

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
