from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DateRange")


@_attrs_define
class DateRange:
    """
    Attributes:
        key (str):
        from_ (Union[Unset, str]):
        to (Union[Unset, str]):
    """

    key: str
    from_: Union[Unset, str] = UNSET
    to: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        from_ = self.from_

        to = self.to

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "key": key,
            }
        )
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        from_ = d.pop("from", UNSET)

        to = d.pop("to", UNSET)

        date_range = cls(
            key=key,
            from_=from_,
            to=to,
        )

        return date_range
