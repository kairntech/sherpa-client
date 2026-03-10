from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.output_params import OutputParams
    from ..models.search_params import SearchParams


T = TypeVar("T", bound="DocSearchRequest")


@_attrs_define
class DocSearchRequest:
    """Document search request

    Attributes:
        output (Union[Unset, OutputParams]): Search output parameters
        search (Union[Unset, SearchParams]): Search parameters
    """

    output: Union[Unset, "OutputParams"] = UNSET
    search: Union[Unset, "SearchParams"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        output: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.output, Unset):
            output = self.output.to_dict()

        search: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.search, Unset):
            search = self.search.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if output is not UNSET:
            field_dict["output"] = output
        if search is not UNSET:
            field_dict["search"] = search

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.output_params import OutputParams
        from ..models.search_params import SearchParams

        d = dict(src_dict)
        _output = d.pop("output", UNSET)
        output: Union[Unset, OutputParams]
        if isinstance(_output, Unset):
            output = UNSET
        else:
            output = OutputParams.from_dict(_output)

        _search = d.pop("search", UNSET)
        search: Union[Unset, SearchParams]
        if isinstance(_search, Unset):
            search = UNSET
        else:
            search = SearchParams.from_dict(_search)

        doc_search_request = cls(
            output=output,
            search=search,
        )

        return doc_search_request
