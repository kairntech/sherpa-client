from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.classification_options import ClassificationOptions


T = TypeVar("T", bound="ConfigPatchOptions")


@attr.s(auto_attribs=True)
class ConfigPatchOptions:
    """
    Attributes:
        classification (Union[Unset, ClassificationOptions]):
        collaborative_annotation (Union[Unset, bool]):
        created_date (Union[Unset, str]):
        description (Union[Unset, str]):
        image_filename (Union[Unset, str]):
        image_id (Union[Unset, str]):
        image_url (Union[Unset, str]):
        label (Union[Unset, str]):
        metafacets (Union[Unset, List[str]]):
        route_on_open_project (Union[Unset, str]):
    """

    classification: Union[Unset, "ClassificationOptions"] = UNSET
    collaborative_annotation: Union[Unset, bool] = UNSET
    created_date: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    image_filename: Union[Unset, str] = UNSET
    image_id: Union[Unset, str] = UNSET
    image_url: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    metafacets: Union[Unset, List[str]] = UNSET
    route_on_open_project: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        classification: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.classification, Unset):
            classification = self.classification.to_dict()

        collaborative_annotation = self.collaborative_annotation
        created_date = self.created_date
        description = self.description
        image_filename = self.image_filename
        image_id = self.image_id
        image_url = self.image_url
        label = self.label
        metafacets: Union[Unset, List[str]] = UNSET
        if not isinstance(self.metafacets, Unset):
            metafacets = self.metafacets

        route_on_open_project = self.route_on_open_project

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if classification is not UNSET:
            field_dict["classification"] = classification
        if collaborative_annotation is not UNSET:
            field_dict["collaborativeAnnotation"] = collaborative_annotation
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if description is not UNSET:
            field_dict["description"] = description
        if image_filename is not UNSET:
            field_dict["imageFilename"] = image_filename
        if image_id is not UNSET:
            field_dict["imageId"] = image_id
        if image_url is not UNSET:
            field_dict["imageUrl"] = image_url
        if label is not UNSET:
            field_dict["label"] = label
        if metafacets is not UNSET:
            field_dict["metafacets"] = metafacets
        if route_on_open_project is not UNSET:
            field_dict["routeOnOpenProject"] = route_on_open_project

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.classification_options import ClassificationOptions

        d = src_dict.copy()
        _classification = d.pop("classification", UNSET)
        classification: Union[Unset, ClassificationOptions]
        if isinstance(_classification, Unset):
            classification = UNSET
        else:
            classification = ClassificationOptions.from_dict(_classification)

        collaborative_annotation = d.pop("collaborativeAnnotation", UNSET)

        created_date = d.pop("createdDate", UNSET)

        description = d.pop("description", UNSET)

        image_filename = d.pop("imageFilename", UNSET)

        image_id = d.pop("imageId", UNSET)

        image_url = d.pop("imageUrl", UNSET)

        label = d.pop("label", UNSET)

        metafacets = cast(List[str], d.pop("metafacets", UNSET))

        route_on_open_project = d.pop("routeOnOpenProject", UNSET)

        config_patch_options = cls(
            classification=classification,
            collaborative_annotation=collaborative_annotation,
            created_date=created_date,
            description=description,
            image_filename=image_filename,
            image_id=image_id,
            image_url=image_url,
            label=label,
            metafacets=metafacets,
            route_on_open_project=route_on_open_project,
        )

        return config_patch_options
