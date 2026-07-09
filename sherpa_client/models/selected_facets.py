from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.facet_order import FacetOrder


T = TypeVar("T", bound="SelectedFacets")


@_attrs_define
class SelectedFacets:
    """Search selected facets parameters

    Attributes:
        field (Union[Unset, str]):
        include (Union[Unset, str]):
        order (Union[Unset, FacetOrder]): Facet aggregation order
        size (Union[Unset, int]):
    """

    field: Union[Unset, str] = UNSET
    include: Union[Unset, str] = UNSET
    order: Union[Unset, "FacetOrder"] = UNSET
    size: Union[Unset, int] = UNSET

    def to_dict(self) -> dict[str, Any]:
        field = self.field

        include = self.include

        order: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.order, Unset):
            order = self.order.to_dict()

        size = self.size

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if field is not UNSET:
            field_dict["field"] = field
        if include is not UNSET:
            field_dict["include"] = include
        if order is not UNSET:
            field_dict["order"] = order
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.facet_order import FacetOrder

        d = dict(src_dict)
        field = d.pop("field", UNSET)

        include = d.pop("include", UNSET)

        _order = d.pop("order", UNSET)
        order: Union[Unset, FacetOrder]
        if isinstance(_order, Unset):
            order = UNSET
        else:
            order = FacetOrder.from_dict(_order)

        size = d.pop("size", UNSET)

        selected_facets = cls(
            field=field,
            include=include,
            order=order,
            size=size,
        )

        return selected_facets
