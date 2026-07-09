from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="FacetOrder")


@_attrs_define
class FacetOrder:
    """Facet aggregation order

    Attributes:
        direction (Union[Unset, str]):  Default: 'desc'.
        key (Union[Unset, str]):  Default: '_count'.
    """

    direction: Union[Unset, str] = "desc"
    key: Union[Unset, str] = "_count"

    def to_dict(self) -> dict[str, Any]:
        direction = self.direction

        key = self.key

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if direction is not UNSET:
            field_dict["direction"] = direction
        if key is not UNSET:
            field_dict["key"] = key

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        direction = d.pop("direction", UNSET)

        key = d.pop("key", UNSET)

        facet_order = cls(
            direction=direction,
            key=key,
        )

        return facet_order
