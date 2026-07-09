from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.metadata_description_entry import MetadataDescriptionEntry


T = TypeVar("T", bound="MetadataDescription")


@_attrs_define
class MetadataDescription:
    """
    Attributes:
        descriptions (list['MetadataDescriptionEntry']):
        name (str):
    """

    descriptions: list["MetadataDescriptionEntry"]
    name: str

    def to_dict(self) -> dict[str, Any]:
        descriptions = []
        for descriptions_item_data in self.descriptions:
            descriptions_item = descriptions_item_data.to_dict()
            descriptions.append(descriptions_item)

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "descriptions": descriptions,
                "name": name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.metadata_description_entry import MetadataDescriptionEntry

        d = dict(src_dict)
        descriptions = []
        _descriptions = d.pop("descriptions")
        for descriptions_item_data in _descriptions:
            descriptions_item = MetadataDescriptionEntry.from_dict(
                descriptions_item_data
            )

            descriptions.append(descriptions_item)

        name = d.pop("name")

        metadata_description = cls(
            descriptions=descriptions,
            name=name,
        )

        return metadata_description
