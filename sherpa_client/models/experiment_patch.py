from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.experiment_patch_parameters import ExperimentPatchParameters


T = TypeVar("T", bound="ExperimentPatch")


@attr.s(auto_attribs=True)
class ExperimentPatch:
    """
    Attributes:
        email_notification (Union[Unset, bool]):
        favorite (Union[Unset, bool]):
        label (Union[Unset, str]):
        parameters (Union[Unset, ExperimentPatchParameters]):
        tags (Union[Unset, List[str]]):
    """

    email_notification: Union[Unset, bool] = UNSET
    favorite: Union[Unset, bool] = UNSET
    label: Union[Unset, str] = UNSET
    parameters: Union[Unset, "ExperimentPatchParameters"] = UNSET
    tags: Union[Unset, List[str]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        email_notification = self.email_notification
        favorite = self.favorite
        label = self.label
        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        tags: Union[Unset, List[str]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if email_notification is not UNSET:
            field_dict["emailNotification"] = email_notification
        if favorite is not UNSET:
            field_dict["favorite"] = favorite
        if label is not UNSET:
            field_dict["label"] = label
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.experiment_patch_parameters import ExperimentPatchParameters

        d = src_dict.copy()
        email_notification = d.pop("emailNotification", UNSET)

        favorite = d.pop("favorite", UNSET)

        label = d.pop("label", UNSET)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, ExperimentPatchParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = ExperimentPatchParameters.from_dict(_parameters)

        tags = cast(List[str], d.pop("tags", UNSET))

        experiment_patch = cls(
            email_notification=email_notification,
            favorite=favorite,
            label=label,
            parameters=parameters,
            tags=tags,
        )

        return experiment_patch
