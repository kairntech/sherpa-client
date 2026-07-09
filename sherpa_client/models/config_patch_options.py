from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_options import ClassificationOptions
    from ..models.config_patch_options_facet_orders import ConfigPatchOptionsFacetOrders


T = TypeVar("T", bound="ConfigPatchOptions")


@_attrs_define
class ConfigPatchOptions:
    """
    Attributes:
        automatic_facets (Union[Unset, bool]):
        automatic_metafacets (Union[Unset, bool]):
        classification (Union[Unset, ClassificationOptions]):
        clean_html (Union[Unset, bool]):
        collaborative_annotation (Union[Unset, bool]):
        created_date (Union[Unset, str]):
        description (Union[Unset, str]):
        document_delta_enabled (Union[Unset, bool]):
        enabled_facets (Union[Unset, list[str]]):
        facet_orders (Union[Unset, ConfigPatchOptionsFacetOrders]):
        image_filename (Union[Unset, str]):
        image_id (Union[Unset, str]):
        image_url (Union[Unset, str]):
        label (Union[Unset, str]):
        markdown_content (Union[Unset, bool]):
        metafacets (Union[Unset, list[str]]):
        replace_carriage_returns (Union[Unset, bool]):
        route_on_open_project (Union[Unset, str]):
        writes_disabled (Union[Unset, bool]):
    """

    automatic_facets: Union[Unset, bool] = UNSET
    automatic_metafacets: Union[Unset, bool] = UNSET
    classification: Union[Unset, "ClassificationOptions"] = UNSET
    clean_html: Union[Unset, bool] = UNSET
    collaborative_annotation: Union[Unset, bool] = UNSET
    created_date: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    document_delta_enabled: Union[Unset, bool] = UNSET
    enabled_facets: Union[Unset, list[str]] = UNSET
    facet_orders: Union[Unset, "ConfigPatchOptionsFacetOrders"] = UNSET
    image_filename: Union[Unset, str] = UNSET
    image_id: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    markdown_content: Union[Unset, bool] = UNSET
    metafacets: Union[Unset, list[str]] = UNSET
    replace_carriage_returns: Union[Unset, bool] = UNSET
    route_on_open_project: Union[Unset, str] = UNSET
    writes_disabled: Union[Unset, bool] = UNSET

    def to_dict(self) -> dict[str, Any]:
        automatic_facets = self.automatic_facets

        automatic_metafacets = self.automatic_metafacets

        classification: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.classification, Unset):
            classification = self.classification.to_dict()

        clean_html = self.clean_html

        collaborative_annotation = self.collaborative_annotation

        created_date = self.created_date

        description = self.description

        document_delta_enabled = self.document_delta_enabled

        enabled_facets: Union[Unset, list[str]] = UNSET
        if not isinstance(self.enabled_facets, Unset):
            enabled_facets = self.enabled_facets

        facet_orders: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.facet_orders, Unset):
            facet_orders = self.facet_orders.to_dict()

        image_filename = self.image_filename

        image_id = self.image_id

        image_url = self.image_url

        label = self.label

        markdown_content = self.markdown_content

        metafacets: Union[Unset, list[str]] = UNSET
        if not isinstance(self.metafacets, Unset):
            metafacets = self.metafacets

        replace_carriage_returns = self.replace_carriage_returns

        route_on_open_project = self.route_on_open_project

        writes_disabled = self.writes_disabled

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if automatic_facets is not UNSET:
            field_dict["automaticFacets"] = automatic_facets
        if automatic_metafacets is not UNSET:
            field_dict["automaticMetafacets"] = automatic_metafacets
        if classification is not UNSET:
            field_dict["classification"] = classification
        if clean_html is not UNSET:
            field_dict["cleanHtml"] = clean_html
        if collaborative_annotation is not UNSET:
            field_dict["collaborativeAnnotation"] = collaborative_annotation
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if description is not UNSET:
            field_dict["description"] = description
        if document_delta_enabled is not UNSET:
            field_dict["documentDeltaEnabled"] = document_delta_enabled
        if enabled_facets is not UNSET:
            field_dict["enabledFacets"] = enabled_facets
        if facet_orders is not UNSET:
            field_dict["facetOrders"] = facet_orders
        if image_filename is not UNSET:
            field_dict["imageFilename"] = image_filename
        if image_id is not UNSET:
            field_dict["imageId"] = image_id
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if label is not UNSET:
            field_dict["label"] = label
        if markdown_content is not UNSET:
            field_dict["markdownContent"] = markdown_content
        if metafacets is not UNSET:
            field_dict["metafacets"] = metafacets
        if replace_carriage_returns is not UNSET:
            field_dict["replaceCarriageReturns"] = replace_carriage_returns
        if route_on_open_project is not UNSET:
            field_dict["routeOnOpenProject"] = route_on_open_project
        if writes_disabled is not UNSET:
            field_dict["writesDisabled"] = writes_disabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.classification_options import ClassificationOptions
        from ..models.config_patch_options_facet_orders import (
            ConfigPatchOptionsFacetOrders,
        )

        d = dict(src_dict)
        automatic_facets = d.pop("automaticFacets", UNSET)

        automatic_metafacets = d.pop("automaticMetafacets", UNSET)

        _classification = d.pop("classification", UNSET)
        classification: Union[Unset, ClassificationOptions]
        if isinstance(_classification, Unset):
            classification = UNSET
        else:
            classification = ClassificationOptions.from_dict(_classification)

        clean_html = d.pop("cleanHtml", UNSET)

        collaborative_annotation = d.pop("collaborativeAnnotation", UNSET)

        created_date = d.pop("createdDate", UNSET)

        description = d.pop("description", UNSET)

        document_delta_enabled = d.pop("documentDeltaEnabled", UNSET)

        enabled_facets = cast(list[str], d.pop("enabledFacets", UNSET))

        _facet_orders = d.pop("facetOrders", UNSET)
        facet_orders: Union[Unset, ConfigPatchOptionsFacetOrders]
        if isinstance(_facet_orders, Unset):
            facet_orders = UNSET
        else:
            facet_orders = ConfigPatchOptionsFacetOrders.from_dict(_facet_orders)

        image_filename = d.pop("imageFilename", UNSET)

        image_id = d.pop("imageId", UNSET)

        image_url = d.pop("imageUrl", UNSET)

        label = d.pop("label", UNSET)

        markdown_content = d.pop("markdownContent", UNSET)

        metafacets = cast(list[str], d.pop("metafacets", UNSET))

        replace_carriage_returns = d.pop("replaceCarriageReturns", UNSET)

        route_on_open_project = d.pop("routeOnOpenProject", UNSET)

        writes_disabled = d.pop("writesDisabled", UNSET)

        config_patch_options = cls(
            automatic_facets=automatic_facets,
            automatic_metafacets=automatic_metafacets,
            classification=classification,
            clean_html=clean_html,
            collaborative_annotation=collaborative_annotation,
            created_date=created_date,
            description=description,
            document_delta_enabled=document_delta_enabled,
            enabled_facets=enabled_facets,
            facet_orders=facet_orders,
            image_filename=image_filename,
            image_id=image_id,
            image_url=image_url,
            label=label,
            markdown_content=markdown_content,
            metafacets=metafacets,
            replace_carriage_returns=replace_carriage_returns,
            route_on_open_project=route_on_open_project,
            writes_disabled=writes_disabled,
        )

        return config_patch_options
