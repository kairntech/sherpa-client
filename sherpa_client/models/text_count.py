from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="TextCount")


@attr.s(auto_attribs=True)
class TextCount:
    """
    Attributes:
        id (str):
        count (int):
    """

    id: str
    count: int

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        count = self.count

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "_id": id,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("_id")

        count = d.pop("count")

        text_count = cls(
            id=id,
            count=count,
        )

        return text_count
