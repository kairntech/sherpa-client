from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.annotated_doc_alt_text import AnnotatedDocAltText
    from ..models.annotated_doc_annotation import AnnotatedDocAnnotation
    from ..models.annotated_doc_category import AnnotatedDocCategory
    from ..models.annotated_doc_sentence import AnnotatedDocSentence
    from ..models.annotated_document_metadata import AnnotatedDocumentMetadata
    from ..models.named_vector import NamedVector


T = TypeVar("T", bound="AnnotatedDocument")


@attr.s(auto_attribs=True)
class AnnotatedDocument:
    """
    Attributes:
        text (str): text of the document
        alt_texts (Union[Unset, List['AnnotatedDocAltText']]):
        annotations (Union[Unset, List['AnnotatedDocAnnotation']]):
        categories (Union[Unset, List['AnnotatedDocCategory']]):
        identifier (Union[Unset, str]): document identifier (externally provided or generated by sherpa)
        metadata (Union[Unset, AnnotatedDocumentMetadata]): document metadata
        sentences (Union[Unset, List['AnnotatedDocSentence']]):
        title (Union[Unset, str]): document title
        vectors (Union[Unset, List['NamedVector']]):
    """

    text: str
    alt_texts: Union[Unset, List["AnnotatedDocAltText"]] = UNSET
    annotations: Union[Unset, List["AnnotatedDocAnnotation"]] = UNSET
    categories: Union[Unset, List["AnnotatedDocCategory"]] = UNSET
    identifier: Union[Unset, str] = UNSET
    metadata: Union[Unset, "AnnotatedDocumentMetadata"] = UNSET
    sentences: Union[Unset, List["AnnotatedDocSentence"]] = UNSET
    title: Union[Unset, str] = UNSET
    vectors: Union[Unset, List["NamedVector"]] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        text = self.text
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
        vectors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vectors, Unset):
            vectors = []
            for vectors_item_data in self.vectors:
                vectors_item = vectors_item_data.to_dict()

                vectors.append(vectors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "text": text,
            }
        )
        if alt_texts is not UNSET:
            field_dict["altTexts"] = alt_texts
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
        if vectors is not UNSET:
            field_dict["vectors"] = vectors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.annotated_doc_alt_text import AnnotatedDocAltText
        from ..models.annotated_doc_annotation import AnnotatedDocAnnotation
        from ..models.annotated_doc_category import AnnotatedDocCategory
        from ..models.annotated_doc_sentence import AnnotatedDocSentence
        from ..models.annotated_document_metadata import AnnotatedDocumentMetadata
        from ..models.named_vector import NamedVector

        d = src_dict.copy()
        text = d.pop("text")

        alt_texts = []
        _alt_texts = d.pop("altTexts", UNSET)
        for alt_texts_item_data in _alt_texts or []:
            alt_texts_item = AnnotatedDocAltText.from_dict(alt_texts_item_data)

            alt_texts.append(alt_texts_item)

        annotations = []
        _annotations = d.pop("annotations", UNSET)
        for annotations_item_data in _annotations or []:
            annotations_item = AnnotatedDocAnnotation.from_dict(annotations_item_data)

            annotations.append(annotations_item)

        categories = []
        _categories = d.pop("categories", UNSET)
        for categories_item_data in _categories or []:
            categories_item = AnnotatedDocCategory.from_dict(categories_item_data)

            categories.append(categories_item)

        identifier = d.pop("identifier", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, AnnotatedDocumentMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = AnnotatedDocumentMetadata.from_dict(_metadata)

        sentences = []
        _sentences = d.pop("sentences", UNSET)
        for sentences_item_data in _sentences or []:
            sentences_item = AnnotatedDocSentence.from_dict(sentences_item_data)

            sentences.append(sentences_item)

        title = d.pop("title", UNSET)

        vectors = []
        _vectors = d.pop("vectors", UNSET)
        for vectors_item_data in _vectors or []:
            vectors_item = NamedVector.from_dict(vectors_item_data)

            vectors.append(vectors_item)

        annotated_document = cls(
            text=text,
            alt_texts=alt_texts,
            annotations=annotations,
            categories=categories,
            identifier=identifier,
            metadata=metadata,
            sentences=sentences,
            title=title,
            vectors=vectors,
        )

        return annotated_document
