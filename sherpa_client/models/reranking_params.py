from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RerankingParams")


@_attrs_define
class RerankingParams:
    """Reranking parameters

    Attributes:
        enabled (Union[Unset, bool]): Rerank hits Default: False.
        reranker (Union[Unset, str]): Reranker to be used
        search_size (Union[Unset, int]): Actual search limit that will be used: when non-zero it takes the precedence
            over limitFactor Default: 0.
        search_size_factor (Union[Unset, int]): Multiplication factor of 'search limit' to search beyond the limit then
            rerank and keep only 'search limit' hits Default: 5.
    """

    enabled: Union[Unset, bool] = False
    reranker: Union[Unset, str] = UNSET
    search_size: Union[Unset, int] = 0
    search_size_factor: Union[Unset, int] = 5

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        reranker = self.reranker

        search_size = self.search_size

        search_size_factor = self.search_size_factor

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if reranker is not UNSET:
            field_dict["reranker"] = reranker
        if search_size is not UNSET:
            field_dict["searchSize"] = search_size
        if search_size_factor is not UNSET:
            field_dict["searchSizeFactor"] = search_size_factor

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        reranker = d.pop("reranker", UNSET)

        search_size = d.pop("searchSize", UNSET)

        search_size_factor = d.pop("searchSizeFactor", UNSET)

        reranking_params = cls(
            enabled=enabled,
            reranker=reranker,
            search_size=search_size,
            search_size_factor=search_size_factor,
        )

        return reranking_params
