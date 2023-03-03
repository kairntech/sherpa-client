from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.converter import Converter
    from ..models.formatter import Formatter
    from ..models.segmenter import Segmenter
    from ..models.with_annotator import WithAnnotator
    from ..models.with_converter import WithConverter
    from ..models.with_language_guesser import WithLanguageGuesser
    from ..models.with_processor import WithProcessor
    from ..models.with_segmenter import WithSegmenter


T = TypeVar("T", bound="AnnotationPlan")


@attr.s(auto_attribs=True)
class AnnotationPlan:
    """
    Attributes:
        pipeline (List[Union['WithAnnotator', 'WithConverter', 'WithLanguageGuesser', 'WithProcessor',
            'WithSegmenter']]):
        converter (Union[Unset, Converter]):
        formatter (Union[Unset, Formatter]):
        segmenter (Union[Unset, Segmenter]):
    """

    pipeline: List[Union["WithAnnotator", "WithConverter", "WithLanguageGuesser", "WithProcessor", "WithSegmenter"]]
    converter: Union[Unset, "Converter"] = UNSET
    formatter: Union[Unset, "Formatter"] = UNSET
    segmenter: Union[Unset, "Segmenter"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.with_annotator import WithAnnotator
        from ..models.with_language_guesser import WithLanguageGuesser
        from ..models.with_processor import WithProcessor
        from ..models.with_segmenter import WithSegmenter

        pipeline = []
        for pipeline_item_data in self.pipeline:
            pipeline_item: Dict[str, Any]

            if isinstance(pipeline_item_data, WithAnnotator):
                pipeline_item = pipeline_item_data.to_dict()

            elif isinstance(pipeline_item_data, WithProcessor):
                pipeline_item = pipeline_item_data.to_dict()

            elif isinstance(pipeline_item_data, WithLanguageGuesser):
                pipeline_item = pipeline_item_data.to_dict()

            elif isinstance(pipeline_item_data, WithSegmenter):
                pipeline_item = pipeline_item_data.to_dict()

            else:
                pipeline_item = pipeline_item_data.to_dict()

            pipeline.append(pipeline_item)

        converter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.converter, Unset):
            converter = self.converter.to_dict()

        formatter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.formatter, Unset):
            formatter = self.formatter.to_dict()

        segmenter: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.segmenter, Unset):
            segmenter = self.segmenter.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "pipeline": pipeline,
            }
        )
        if converter is not UNSET:
            field_dict["converter"] = converter
        if formatter is not UNSET:
            field_dict["formatter"] = formatter
        if segmenter is not UNSET:
            field_dict["segmenter"] = segmenter

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.converter import Converter
        from ..models.formatter import Formatter
        from ..models.segmenter import Segmenter
        from ..models.with_annotator import WithAnnotator
        from ..models.with_converter import WithConverter
        from ..models.with_language_guesser import WithLanguageGuesser
        from ..models.with_processor import WithProcessor
        from ..models.with_segmenter import WithSegmenter

        d = src_dict.copy()
        pipeline = []
        _pipeline = d.pop("pipeline")
        for pipeline_item_data in _pipeline:

            def _parse_pipeline_item(
                data: object,
            ) -> Union["WithAnnotator", "WithConverter", "WithLanguageGuesser", "WithProcessor", "WithSegmenter"]:
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
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    pipeline_item_type_3 = WithSegmenter.from_dict(data)

                    return pipeline_item_type_3
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                pipeline_item_type_4 = WithConverter.from_dict(data)

                return pipeline_item_type_4

            pipeline_item = _parse_pipeline_item(pipeline_item_data)

            pipeline.append(pipeline_item)

        _converter = d.pop("converter", UNSET)
        converter: Union[Unset, Converter]
        if isinstance(_converter, Unset):
            converter = UNSET
        else:
            converter = Converter.from_dict(_converter)

        _formatter = d.pop("formatter", UNSET)
        formatter: Union[Unset, Formatter]
        if isinstance(_formatter, Unset):
            formatter = UNSET
        else:
            formatter = Formatter.from_dict(_formatter)

        _segmenter = d.pop("segmenter", UNSET)
        segmenter: Union[Unset, Segmenter]
        if isinstance(_segmenter, Unset):
            segmenter = UNSET
        else:
            segmenter = Segmenter.from_dict(_segmenter)

        annotation_plan = cls(
            pipeline=pipeline,
            converter=converter,
            formatter=formatter,
            segmenter=segmenter,
        )

        return annotation_plan
