from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.doc_alt_text import DocAltText
from ..models.doc_annotation import DocAnnotation
from ..models.doc_category import DocCategory
from ..models.doc_sentence import DocSentence
from ..models.document_metadata import DocumentMetadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="Document")


@attr.s(auto_attribs=True)
class Document:
    """ """

    identifier: str
    text: str
    title: str
    alt_texts: Union[Unset, List[DocAltText]] = UNSET
    annotations: Union[Unset, List[DocAnnotation]] = UNSET
    categories: Union[Unset, List[DocCategory]] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_date: Union[Unset, str] = UNSET
    metadata: Union[Unset, DocumentMetadata] = UNSET
    modified_date: Union[Unset, str] = UNSET
    sentences: Union[Unset, List[DocSentence]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        identifier = self.identifier
        text = self.text
        title = self.title
        alt_texts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.alt_texts, Unset):
            alt_texts = []
            for alt_texts_item_data in self.alt_texts:
                alt_texts_item = alt_texts_item_data.to_dict()

                alt_texts.append(alt_texts_item)

        annotations: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.annotations, Unset):
            annotations = []
            for annotations_item_data in self.annotations:
                annotations_item = annotations_item_data.to_dict()

                annotations.append(annotations_item)

        categories: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()

                categories.append(categories_item)

        created_by = self.created_by
        created_date = self.created_date
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        modified_date = self.modified_date
        sentences: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sentences, Unset):
            sentences = []
            for sentences_item_data in self.sentences:
                sentences_item = sentences_item_data.to_dict()

                sentences.append(sentences_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "identifier": identifier,
                "text": text,
                "title": title,
            }
        )
        if alt_texts is not UNSET:
            field_dict["altTexts"] = alt_texts
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if categories is not UNSET:
            field_dict["categories"] = categories
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if modified_date is not UNSET:
            field_dict["modifiedDate"] = modified_date
        if sentences is not UNSET:
            field_dict["sentences"] = sentences

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifier = d.pop("identifier")

        text = d.pop("text")

        title = d.pop("title")

        alt_texts = []
        _alt_texts = d.pop("altTexts", UNSET)
        for alt_texts_item_data in _alt_texts or []:
            alt_texts_item = DocAltText.from_dict(alt_texts_item_data)

            alt_texts.append(alt_texts_item)

        annotations = []
        _annotations = d.pop("annotations", UNSET)
        for annotations_item_data in _annotations or []:
            annotations_item = DocAnnotation.from_dict(annotations_item_data)

            annotations.append(annotations_item)

        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = DocCategory.from_dict(categories_item_data)

            categories.append(categories_item)

        created_by = d.pop("createdBy", UNSET)

        created_date = d.pop("createdDate", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, DocumentMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = DocumentMetadata.from_dict(_metadata)

        modified_date = d.pop("modifiedDate", UNSET)

        sentences = []
        _sentences = d.pop("sentences", UNSET)
        for sentences_item_data in _sentences or []:
            sentences_item = DocSentence.from_dict(sentences_item_data)

            sentences.append(sentences_item)

        document = cls(
            identifier=identifier,
            text=text,
            title=title,
            alt_texts=alt_texts,
            annotations=annotations,
            categories=categories,
            created_by=created_by,
            created_date=created_date,
            metadata=metadata,
            modified_date=modified_date,
            sentences=sentences,
        )

        return document
