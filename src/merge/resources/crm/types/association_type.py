# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ....core.datetime_utils import serialize_datetime
from .association_sub_type import AssociationSubType
from .association_type_cardinality import AssociationTypeCardinality

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AssociationType(pydantic.BaseModel):
    """
    # The AssociationType Object

    ### Description

    The `Association Type` object represents the relationship between two objects.

    ### Usage Example

    TODO
    """

    source_object_class: typing.Optional[typing.Dict[str, typing.Any]]
    target_object_classes: typing.Optional[typing.List[AssociationSubType]]
    remote_key_name: typing.Optional[str]
    display_name: typing.Optional[str]
    cardinality: typing.Optional[AssociationTypeCardinality]
    is_required: typing.Optional[bool]
    id: typing.Optional[str]
    remote_id: typing.Optional[str] = pydantic.Field(description="The third-party API ID of the matching object.")
    created_at: typing.Optional[dt.datetime]
    modified_at: typing.Optional[dt.datetime] = pydantic.Field(
        description="This is the datetime that this object was last updated by Merge"
    )

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
