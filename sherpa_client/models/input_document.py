from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.doc_annotation import DocAnnotation
from ..models.doc_category import DocCategory
from ..models.doc_sentence import DocSentence
from ..models.input_document_al_texts import InputDocumentAlTexts
from ..models.input_document_metadata import InputDocumentMetadata
from ..types import UNSET, Unset

T = TypeVar("T", bound="InputDocument")


@attr.s(auto_attribs=True)
class InputDocument:
    """ """

    text: str
    al_texts: Union[Unset, InputDocumentAlTexts] = UNSET
    annotations: Union[Unset, List[DocAnnotation]] = UNSET
    categories: Union[Unset, List[DocCategory]] = UNSET
    identifier: Union[Unset, str] = UNSET
    metadata: Union[Unset, InputDocumentMetadata] = UNSET
    sentences: Union[Unset, List[DocSentence]] = UNSET
    title: Union[Unset, str] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
        al_texts: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.al_texts, Unset):
            al_texts = self.al_texts.to_dict()

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

        identifier = self.identifier
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        sentences: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.sentences, Unset):
            sentences = []
            for sentences_item_data in self.sentences:
                sentences_item = sentences_item_data.to_dict()

                sentences.append(sentences_item)

        title = self.title

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "text": text,
            }
        )
        if al_texts is not UNSET:
            field_dict["alTexts"] = al_texts
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if categories is not UNSET:
            field_dict["categories"] = categories
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if sentences is not UNSET:
            field_dict["sentences"] = sentences
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        text = d.pop("text")

        _al_texts = d.pop("alTexts", UNSET)
        al_texts: Union[Unset, InputDocumentAlTexts]
        if isinstance(_al_texts, Unset):
            al_texts = UNSET
        else:
            al_texts = InputDocumentAlTexts.from_dict(_al_texts)

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

        identifier = d.pop("identifier", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, InputDocumentMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = InputDocumentMetadata.from_dict(_metadata)

        sentences = []
        _sentences = d.pop("sentences", UNSET)
        for sentences_item_data in _sentences or []:
            sentences_item = DocSentence.from_dict(sentences_item_data)

            sentences.append(sentences_item)

        title = d.pop("title", UNSET)

        input_document = cls(
            text=text,
            al_texts=al_texts,
            annotations=annotations,
            categories=categories,
            identifier=identifier,
            metadata=metadata,
            sentences=sentences,
            title=title,
        )

        return input_document
