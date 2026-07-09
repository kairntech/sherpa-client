from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.date_range_config import DateRangeConfig
    from ..models.significant_text_config import SignificantTextConfig
    from ..models.terms_config import TermsConfig


T = TypeVar("T", bound="FacetConfiguration")


@_attrs_define
class FacetConfiguration:
    """
    Attributes:
        name (str):
        date_range (Union[Unset, DateRangeConfig]):
        enabled (Union[Unset, bool]):  Default: True.
        grouped_by_user (Union[Unset, bool]):
        multi_user (Union[Unset, bool]):
        natures (Union[Unset, str]):
        significant_text (Union[Unset, SignificantTextConfig]):
        terms (Union[Unset, TermsConfig]):
    """

    name: str
    date_range: Union[Unset, "DateRangeConfig"] = UNSET
    enabled: Union[Unset, bool] = True
    grouped_by_user: Union[Unset, bool] = UNSET
    multi_user: Union[Unset, bool] = UNSET
    natures: Union[Unset, str] = UNSET
    significant_text: Union[Unset, "SignificantTextConfig"] = UNSET
    terms: Union[Unset, "TermsConfig"] = UNSET

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        date_range: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.date_range, Unset):
            date_range = self.date_range.to_dict()

        enabled = self.enabled

        grouped_by_user = self.grouped_by_user

        multi_user = self.multi_user

        natures = self.natures

        significant_text: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.significant_text, Unset):
            significant_text = self.significant_text.to_dict()

        terms: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.terms, Unset):
            terms = self.terms.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "name": name,
            }
        )
        if date_range is not UNSET:
            field_dict["dateRange"] = date_range
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if grouped_by_user is not UNSET:
            field_dict["groupedByUser"] = grouped_by_user
        if multi_user is not UNSET:
            field_dict["multiUser"] = multi_user
        if natures is not UNSET:
            field_dict["natures"] = natures
        if significant_text is not UNSET:
            field_dict["significantText"] = significant_text
        if terms is not UNSET:
            field_dict["terms"] = terms

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.date_range_config import DateRangeConfig
        from ..models.significant_text_config import SignificantTextConfig
        from ..models.terms_config import TermsConfig

        d = dict(src_dict)
        name = d.pop("name")

        _date_range = d.pop("dateRange", UNSET)
        date_range: Union[Unset, DateRangeConfig]
        if isinstance(_date_range, Unset):
            date_range = UNSET
        else:
            date_range = DateRangeConfig.from_dict(_date_range)

        enabled = d.pop("enabled", UNSET)

        grouped_by_user = d.pop("groupedByUser", UNSET)

        multi_user = d.pop("multiUser", UNSET)

        natures = d.pop("natures", UNSET)

        _significant_text = d.pop("significantText", UNSET)
        significant_text: Union[Unset, SignificantTextConfig]
        if isinstance(_significant_text, Unset):
            significant_text = UNSET
        else:
            significant_text = SignificantTextConfig.from_dict(_significant_text)

        _terms = d.pop("terms", UNSET)
        terms: Union[Unset, TermsConfig]
        if isinstance(_terms, Unset):
            terms = UNSET
        else:
            terms = TermsConfig.from_dict(_terms)

        facet_configuration = cls(
            name=name,
            date_range=date_range,
            enabled=enabled,
            grouped_by_user=grouped_by_user,
            multi_user=multi_user,
            natures=natures,
            significant_text=significant_text,
            terms=terms,
        )

        return facet_configuration
