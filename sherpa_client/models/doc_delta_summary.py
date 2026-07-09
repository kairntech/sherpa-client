from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="DocDeltaSummary")


@_attrs_define
class DocDeltaSummary:
    """
    Attributes:
        deleted (int):
        modified (int):
        first_update_at (Union[Unset, str]):
        last_start (Union[Unset, str]):
        last_update_at (Union[Unset, str]):
    """

    deleted: int
    modified: int
    first_update_at: Union[Unset, str] = UNSET
    last_start: Union[Unset, str] = UNSET
    last_update_at: Union[Unset, str] = UNSET

    def to_dict(self) -> dict[str, Any]:
        deleted = self.deleted

        modified = self.modified

        first_update_at = self.first_update_at

        last_start = self.last_start

        last_update_at = self.last_update_at

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "deleted": deleted,
                "modified": modified,
            }
        )
        if first_update_at is not UNSET:
            field_dict["firstUpdateAt"] = first_update_at
        if last_start is not UNSET:
            field_dict["lastStart"] = last_start
        if last_update_at is not UNSET:
            field_dict["lastUpdateAt"] = last_update_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deleted = d.pop("deleted")

        modified = d.pop("modified")

        first_update_at = d.pop("firstUpdateAt", UNSET)

        last_start = d.pop("lastStart", UNSET)

        last_update_at = d.pop("lastUpdateAt", UNSET)

        doc_delta_summary = cls(
            deleted=deleted,
            modified=modified,
            first_update_at=first_update_at,
            last_start=last_start,
            last_update_at=last_update_at,
        )

        return doc_delta_summary
