from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="DownloadLink")


@_attrs_define
class DownloadLink:
    """
    Attributes:
        content_type (str):
        delete_after_download (bool):
        filename (str):
    """

    content_type: str
    delete_after_download: bool
    filename: str

    def to_dict(self) -> dict[str, Any]:
        content_type = self.content_type

        delete_after_download = self.delete_after_download

        filename = self.filename

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "contentType": content_type,
                "deleteAfterDownload": delete_after_download,
                "filename": filename,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content_type = d.pop("contentType")

        delete_after_download = d.pop("deleteAfterDownload")

        filename = d.pop("filename")

        download_link = cls(
            content_type=content_type,
            delete_after_download=delete_after_download,
            filename=filename,
        )

        return download_link
