from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

if TYPE_CHECKING:
    from ..models.formatter import Formatter
    from ..models.input_document import InputDocument
    from ..models.with_annotator import WithAnnotator
    from ..models.with_language_guesser import WithLanguageGuesser
    from ..models.with_processor import WithProcessor
    from ..models.with_segmenter import WithSegmenter


T = TypeVar("T", bound="FormatDocumentsWithMany")


@attr.s(auto_attribs=True)
class FormatDocumentsWithMany:
    """
    Attributes:
        documents (List['InputDocument']):
        formatter (Formatter):
        pipeline (List[Union['WithAnnotator', 'WithLanguageGuesser', 'WithProcessor', 'WithSegmenter']]):
    """

    documents: List["InputDocument"]
    formatter: "Formatter"
    pipeline: List[Union["WithAnnotator", "WithLanguageGuesser", "WithProcessor", "WithSegmenter"]]

    def to_dict(self) -> Dict[str, Any]:
        from ..models.with_annotator import WithAnnotator
        from ..models.with_language_guesser import WithLanguageGuesser
        from ..models.with_processor import WithProcessor

        documents = []
        for documents_item_data in self.documents:
            documents_item = documents_item_data.to_dict()

            documents.append(documents_item)

        formatter = self.formatter.to_dict()

        pipeline = []
        for pipeline_item_data in self.pipeline:
            pipeline_item: Dict[str, Any]

            if isinstance(pipeline_item_data, WithAnnotator):
                pipeline_item = pipeline_item_data.to_dict()

            elif isinstance(pipeline_item_data, WithProcessor):
                pipeline_item = pipeline_item_data.to_dict()

            elif isinstance(pipeline_item_data, WithLanguageGuesser):
                pipeline_item = pipeline_item_data.to_dict()

            else:
                pipeline_item = pipeline_item_data.to_dict()

            pipeline.append(pipeline_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "documents": documents,
                "formatter": formatter,
                "pipeline": pipeline,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.formatter import Formatter
        from ..models.input_document import InputDocument
        from ..models.with_annotator import WithAnnotator
        from ..models.with_language_guesser import WithLanguageGuesser
        from ..models.with_processor import WithProcessor
        from ..models.with_segmenter import WithSegmenter

        d = src_dict.copy()
        documents = []
        _documents = d.pop("documents")
        for documents_item_data in _documents:
            documents_item = InputDocument.from_dict(documents_item_data)

            documents.append(documents_item)

        formatter = Formatter.from_dict(d.pop("formatter"))

        pipeline = []
        _pipeline = d.pop("pipeline")
        for pipeline_item_data in _pipeline:

            def _parse_pipeline_item(
                data: object,
            ) -> Union["WithAnnotator", "WithLanguageGuesser", "WithProcessor", "WithSegmenter"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    pipeline_item_type_0 = WithAnnotator.from_dict(data)

                    return pipeline_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    pipeline_item_type_1 = WithProcessor.from_dict(data)

                    return pipeline_item_type_1
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    pipeline_item_type_2 = WithLanguageGuesser.from_dict(data)

                    return pipeline_item_type_2
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                pipeline_item_type_3 = WithSegmenter.from_dict(data)

                return pipeline_item_type_3

            pipeline_item = _parse_pipeline_item(pipeline_item_data)

            pipeline.append(pipeline_item)

        format_documents_with_many = cls(
            documents=documents,
            formatter=formatter,
            pipeline=pipeline,
        )

        return format_documents_with_many
