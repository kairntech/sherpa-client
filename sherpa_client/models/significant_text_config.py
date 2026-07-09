from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SignificantTextConfig")


@_attrs_define
class SignificantTextConfig:
    """
    Attributes:
        field (str):
        min_doc_count (str):
        size (int):
        filter_duplicate_text (Union[Unset, bool]):
    """

    field: str
    min_doc_count: str
    size: int
    filter_duplicate_text: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        min_doc_count = self.min_doc_count

        size = self.size

        filter_duplicate_text = self.filter_duplicate_text

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "field": field,
                "minDocCount": min_doc_count,
                "size": size,
            }
        )
        if filter_duplicate_text is not UNSET:
            field_dict["filterDuplicateText"] = filter_duplicate_text

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field = d.pop("field")

        min_doc_count = d.pop("minDocCount")

        size = d.pop("size")

        filter_duplicate_text = d.pop("filterDuplicateText", UNSET)

        significant_text_config = cls(
            field=field,
            min_doc_count=min_doc_count,
            size=size,
            filter_duplicate_text=filter_duplicate_text,
        )

        return significant_text_config
