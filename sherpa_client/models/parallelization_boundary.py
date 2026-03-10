from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ParallelizationBoundary")


@_attrs_define
class ParallelizationBoundary:
    """
    Attributes:
        parallelization_boundary (bool):
    """

    parallelization_boundary: bool

    def to_dict(self) -> dict[str, Any]:
        parallelization_boundary = self.parallelization_boundary

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "parallelizationBoundary": parallelization_boundary,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        parallelization_boundary = d.pop("parallelizationBoundary")

        parallelization_boundary = cls(
            parallelization_boundary=parallelization_boundary,
        )

        return parallelization_boundary
