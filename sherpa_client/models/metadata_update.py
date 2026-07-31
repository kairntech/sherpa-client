from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.metadata_update_operation import MetadataUpdateOperation
from ..types import UNSET, Unset

T = TypeVar("T", bound="MetadataUpdate")


@_attrs_define
class MetadataUpdate:
    """
    Attributes:
        name (str): name of the metadata
        operation (Union[Unset, MetadataUpdateOperation]): operation: ADD_METADATA appends all provided values to the
            array, REMOVE_METADATA_VALUE removes the first provided value, REPLACE_METADATA_VALUE sets the metadata to the
            first provided value, REMOVE_METADATA removes the metadata key entirely. When absent, inferred: non-empty values
            → REPLACE_METADATA_VALUE, empty/null → REMOVE_METADATA
        values (Union[Unset, list[str]]):
    """

    name: str
    operation: Union[Unset, MetadataUpdateOperation] = UNSET
    values: Union[Unset, list[str]] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        operation: Union[Unset, str] = UNSET
        if not isinstance(self.operation, Unset):
            operation = self.operation.value

        values: Union[Unset, list[str]] = UNSET
        if not isinstance(self.values, Unset):
            values = self.values

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
            }
        )
        if operation is not UNSET:
            field_dict["operation"] = operation
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        _operation = d.pop("operation", UNSET)
        operation: Union[Unset, MetadataUpdateOperation]
        if isinstance(_operation, Unset):
            operation = UNSET
        else:
            operation = MetadataUpdateOperation(_operation)

        values = cast(list[str], d.pop("values", UNSET))

        metadata_update = cls(
            name=name,
            operation=operation,
            values=values,
        )

        return metadata_update
