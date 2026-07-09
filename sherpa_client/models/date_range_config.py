from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_range import DateRange


T = TypeVar("T", bound="DateRangeConfig")


@_attrs_define
class DateRangeConfig:
    """
    Attributes:
        field (str):
        format_ (str):
        keyed (Union[Unset, bool]):
        missing (Union[Unset, str]):
        ranges (Union[Unset, list['DateRange']]):
    """

    field: str
    format_: str
    keyed: Union[Unset, bool] = UNSET
    missing: Union[Unset, str] = UNSET
    ranges: Union[Unset, list["DateRange"]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        format_ = self.format_

        keyed = self.keyed

        missing = self.missing

        ranges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.ranges, Unset):
            ranges = []
            for ranges_item_data in self.ranges:
                ranges_item = ranges_item_data.to_dict()
                ranges.append(ranges_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "field": field,
                "format": format_,
            }
        )
        if keyed is not UNSET:
            field_dict["keyed"] = keyed
        if missing is not UNSET:
            field_dict["missing"] = missing
        if ranges is not UNSET:
            field_dict["ranges"] = ranges

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.date_range import DateRange

        d = dict(src_dict)
        field = d.pop("field")

        format_ = d.pop("format")

        keyed = d.pop("keyed", UNSET)

        missing = d.pop("missing", UNSET)

        ranges = []
        _ranges = d.pop("ranges", UNSET)
        for ranges_item_data in _ranges or []:
            ranges_item = DateRange.from_dict(ranges_item_data)

            ranges.append(ranges_item)

        date_range_config = cls(
            field=field,
            format_=format_,
            keyed=keyed,
            missing=missing,
            ranges=ranges,
        )

        return date_range_config
