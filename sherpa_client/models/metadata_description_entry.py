from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="MetadataDescriptionEntry")


@_attrs_define
class MetadataDescriptionEntry:
    """
    Attributes:
        language (str):
        text (str):
    """

    language: str
    text: str

    def to_dict(self) -> dict[str, Any]:
        language = self.language

        text = self.text

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "language": language,
                "text": text,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        language = d.pop("language")

        text = d.pop("text")

        metadata_description_entry = cls(
            language=language,
            text=text,
        )

        return metadata_description_entry
