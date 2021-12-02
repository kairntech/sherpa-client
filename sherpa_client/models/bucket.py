from typing import Any, Dict, Type, TypeVar

import attr

T = TypeVar("T", bound="Bucket")


@attr.s(auto_attribs=True)
class Bucket:
    """ """

    key: str
    doc_count: int

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        doc_count = self.doc_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "key": key,
                "doc_count": doc_count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key")

        doc_count = d.pop("doc_count")

        bucket = cls(
            key=key,
            doc_count=doc_count,
        )

        return bucket
