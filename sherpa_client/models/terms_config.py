from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.terms_config_order import TermsConfigOrder


T = TypeVar("T", bound="TermsConfig")


@_attrs_define
class TermsConfig:
    """
    Attributes:
        field (str):
        min_doc_count (Union[Unset, int]):
        missing (Union[Unset, str]):
        order (Union[Unset, TermsConfigOrder]):
        size (Union[Unset, int]):
    """

    field: str
    min_doc_count: Union[Unset, int] = UNSET
    missing: Union[Unset, str] = UNSET
    order: Union[Unset, "TermsConfigOrder"] = UNSET
    size: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        min_doc_count = self.min_doc_count

        missing = self.missing

        order: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "field": field,
            }
        )
        if min_doc_count is not UNSET:
            field_dict["minDocCount"] = min_doc_count
        if missing is not UNSET:
            field_dict["missing"] = missing
        if order is not UNSET:
            field_dict["order"] = order
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.terms_config_order import TermsConfigOrder

        d = dict(src_dict)
        field = d.pop("field")

        min_doc_count = d.pop("minDocCount", UNSET)

        missing = d.pop("missing", UNSET)

        _order = d.pop("order", UNSET)
        order: Union[Unset, TermsConfigOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = TermsConfigOrder.from_dict(_order)

        size = d.pop("size", UNSET)

        terms_config = cls(
            field=field,
            min_doc_count=min_doc_count,
            missing=missing,
            order=order,
            size=size,
        )

        return terms_config
