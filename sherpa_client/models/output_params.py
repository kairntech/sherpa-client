from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="OutputParams")


@_attrs_define
class OutputParams:
    """Search output parameters

    Attributes:
        facets (Union[Unset, bool]): Activate faceted search results Default: False.
        fields (Union[Unset, str]): Hit fields to be returned (e.g. 'annotations,categories' or '!text,!metadata')
        highlight (Union[Unset, bool]): Highlight query terms Default: False.
        html (Union[Unset, bool]):
        random_hits_if_empty_query (Union[Unset, bool]): Return random hits when query is empty Default: True.
        return_hits (Union[Unset, bool]): Return hits in addition to answering the question Default: True.
        return_total (Union[Unset, bool]): Return total number of hits Default: True.
    """

    facets: Union[Unset, bool] = False
    fields: Union[Unset, str] = UNSET
    highlight: Union[Unset, bool] = False
    html: Union[Unset, bool] = UNSET
    random_hits_if_empty_query: Union[Unset, bool] = True
    return_hits: Union[Unset, bool] = True
    return_total: Union[Unset, bool] = True

    def to_dict(self) -> dict[str, Any]:
        facets = self.facets

        fields = self.fields

        highlight = self.highlight

        html = self.html

        random_hits_if_empty_query = self.random_hits_if_empty_query

        return_hits = self.return_hits

        return_total = self.return_total

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if facets is not UNSET:
            field_dict["facets"] = facets
        if fields is not UNSET:
            field_dict["fields"] = fields
        if highlight is not UNSET:
            field_dict["highlight"] = highlight
        if html is not UNSET:
            field_dict["html"] = html
        if random_hits_if_empty_query is not UNSET:
            field_dict["randomHitsIfEmptyQuery"] = random_hits_if_empty_query
        if return_hits is not UNSET:
            field_dict["returnHits"] = return_hits
        if return_total is not UNSET:
            field_dict["returnTotal"] = return_total

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        facets = d.pop("facets", UNSET)

        fields = d.pop("fields", UNSET)

        highlight = d.pop("highlight", UNSET)

        html = d.pop("html", UNSET)

        random_hits_if_empty_query = d.pop("randomHitsIfEmptyQuery", UNSET)

        return_hits = d.pop("returnHits", UNSET)

        return_total = d.pop("returnTotal", UNSET)

        output_params = cls(
            facets=facets,
            fields=fields,
            highlight=highlight,
            html=html,
            random_hits_if_empty_query=random_hits_if_empty_query,
            return_hits=return_hits,
            return_total=return_total,
        )

        return output_params
