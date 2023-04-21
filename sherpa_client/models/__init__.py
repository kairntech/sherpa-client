""" Contains all the data models used in inputs/outputs """

from .ack import Ack
from .aggregation import Aggregation
from .alt_text import AltText
from .annotate_binary_form import AnnotateBinaryForm
from .annotate_binary_with_project_annotator_multipart_data import AnnotateBinaryWithProjectAnnotatorMultipartData
from .annotate_binary_with_project_multipart_data import AnnotateBinaryWithProjectMultipartData
from .annotate_documents_with_pipeline import AnnotateDocumentsWithPipeline
from .annotate_format_binary_with_project_annotator_multipart_data import (
    AnnotateFormatBinaryWithProjectAnnotatorMultipartData,
)
from .annotate_text_with_pipeline import AnnotateTextWithPipeline
from .annotated_doc_alt_text import AnnotatedDocAltText
from .annotated_doc_annotation import AnnotatedDocAnnotation
from .annotated_doc_annotation_creation_mode import AnnotatedDocAnnotationCreationMode
from .annotated_doc_annotation_properties import AnnotatedDocAnnotationProperties
from .annotated_doc_category import AnnotatedDocCategory
from .annotated_doc_category_creation_mode import AnnotatedDocCategoryCreationMode
from .annotated_doc_category_properties import AnnotatedDocCategoryProperties
from .annotated_doc_sentence import AnnotatedDocSentence
from .annotated_doc_sentence_metadata import AnnotatedDocSentenceMetadata
from .annotated_document import AnnotatedDocument
from .annotated_document_metadata import AnnotatedDocumentMetadata
from .annotation import Annotation
from .annotation_creation_mode import AnnotationCreationMode
from .annotation_facets import AnnotationFacets
from .annotation_id import AnnotationId
from .annotation_metrics import AnnotationMetrics
from .annotation_patch import AnnotationPatch
from .annotation_patch_status import AnnotationPatchStatus
from .annotation_plan import AnnotationPlan
from .annotation_status import AnnotationStatus
from .annotation_term import AnnotationTerm
from .annotation_term_properties import AnnotationTermProperties
from .annotator import Annotator
from .annotator_multimap import AnnotatorMultimap
from .apply_to import ApplyTo
from .bearer_token import BearerToken
from .bucket import Bucket
from .categories_facets import CategoriesFacets
from .category import Category
from .category_action import CategoryAction
from .category_creation_mode import CategoryCreationMode
from .category_id import CategoryId
from .category_metrics import CategoryMetrics
from .category_patch import CategoryPatch
from .category_patch_status import CategoryPatchStatus
from .category_status import CategoryStatus
from .classification_config import ClassificationConfig
from .classification_options import ClassificationOptions
from .config_patch_options import ConfigPatchOptions
from .convert_annotation_plan import ConvertAnnotationPlan
from .convert_format_annotation_plan import ConvertFormatAnnotationPlan
from .converter import Converter
from .converter_parameters import ConverterParameters
from .corpus_metrics import CorpusMetrics
from .create_lexicon_response_200 import CreateLexiconResponse200
from .create_project_from_archive_multipart_data import CreateProjectFromArchiveMultipartData
from .create_term_json_body import CreateTermJsonBody
from .create_term_response_200 import CreateTermResponse200
from .created_by_count import CreatedByCount
from .credentials import Credentials
from .delete_group_result import DeleteGroupResult
from .delete_many_response import DeleteManyResponse
from .delete_response import DeleteResponse
from .depends_on import DependsOn
from .deprecated_annotate_binary_with_plan_ref_multipart_data import DeprecatedAnnotateBinaryWithPlanRefMultipartData
from .deprecated_annotate_format_binary_with_plan_ref_multipart_data import (
    DeprecatedAnnotateFormatBinaryWithPlanRefMultipartData,
)
from .doc_alt_text import DocAltText
from .doc_annotation import DocAnnotation
from .doc_annotation_creation_mode import DocAnnotationCreationMode
from .doc_annotation_properties import DocAnnotationProperties
from .doc_annotation_status import DocAnnotationStatus
from .doc_category import DocCategory
from .doc_category_creation_mode import DocCategoryCreationMode
from .doc_category_properties import DocCategoryProperties
from .doc_category_status import DocCategoryStatus
from .doc_sentence import DocSentence
from .doc_sentence_metadata import DocSentenceMetadata
from .document import Document
from .document_facets import DocumentFacets
from .document_hit import DocumentHit
from .document_hits import DocumentHits
from .document_metadata import DocumentMetadata
from .engine_config import EngineConfig
from .engine_config_import_summary import EngineConfigImportSummary
from .engine_name import EngineName
from .error import Error
from .experiment import Experiment
from .experiment_parameters import ExperimentParameters
from .experiment_patch import ExperimentPatch
from .experiment_patch_parameters import ExperimentPatchParameters
from .external_databases import ExternalDatabases
from .external_resources import ExternalResources
from .format_binary_form import FormatBinaryForm
from .format_documents_with_many import FormatDocumentsWithMany
from .format_text_with_many import FormatTextWithMany
from .formatter import Formatter
from .formatter_parameters import FormatterParameters
from .gazetteer import Gazetteer
from .gazetteer_parameters import GazetteerParameters
from .gazetteer_patch import GazetteerPatch
from .gazetteer_patch_parameters import GazetteerPatchParameters
from .group_desc import GroupDesc
from .group_name import GroupName
from .group_patch import GroupPatch
from .group_share import GroupShare
from .http_service_metadata import HttpServiceMetadata
from .http_service_metadata_operations import HttpServiceMetadataOperations
from .http_service_record import HttpServiceRecord
from .import_archive_multipart_data import ImportArchiveMultipartData
from .import_models_multipart_data import ImportModelsMultipartData
from .input_document import InputDocument
from .input_document_metadata import InputDocumentMetadata
from .item_count import ItemCount
from .item_ref import ItemRef
from .label import Label
from .label_count import LabelCount
from .label_names import LabelNames
from .label_set import LabelSet
from .label_set_update import LabelSetUpdate
from .label_update import LabelUpdate
from .launch_document_import_multipart_data import LaunchDocumentImportMultipartData
from .launch_document_import_segmentation_policy import LaunchDocumentImportSegmentationPolicy
from .launch_project_restoration_from_backup_multipart_data import LaunchProjectRestorationFromBackupMultipartData
from .launch_uploaded_document_import_segmentation_policy import LaunchUploadedDocumentImportSegmentationPolicy
from .lexicon import Lexicon
from .lexicon_update import LexiconUpdate
from .maybe_create_projects_and_import_models_from_archive_multipart_data import (
    MaybeCreateProjectsAndImportModelsFromArchiveMultipartData,
)
from .metadata_count import MetadataCount
from .model_metrics import ModelMetrics
from .model_metrics_options import ModelMetricsOptions
from .models_metrics import ModelsMetrics
from .named_annotation_plan import NamedAnnotationPlan
from .new_experiment import NewExperiment
from .new_experiment_parameters import NewExperimentParameters
from .new_gazetteer import NewGazetteer
from .new_gazetteer_parameters import NewGazetteerParameters
from .new_group_desc import NewGroupDesc
from .new_named_annotation_plan import NewNamedAnnotationPlan
from .new_role import NewRole
from .new_suggester import NewSuggester
from .new_suggester_parameters import NewSuggesterParameters
from .new_user import NewUser
from .next_step import NextStep
from .operation_count import OperationCount
from .partial_label import PartialLabel
from .partial_lexicon import PartialLexicon
from .plan_patch import PlanPatch
from .project_annotators import ProjectAnnotators
from .project_bean import ProjectBean
from .project_config_creation import ProjectConfigCreation
from .project_config_creation_properties import ProjectConfigCreationProperties
from .project_open_session import ProjectOpenSession
from .project_open_session_state import ProjectOpenSessionState
from .project_property import ProjectProperty
from .project_status import ProjectStatus
from .projects_annotators import ProjectsAnnotators
from .quality_figures import QualityFigures
from .report import Report
from .report_classes import ReportClasses
from .request_jwt_token_project_access_mode import RequestJwtTokenProjectAccessMode
from .role_desc import RoleDesc
from .role_update import RoleUpdate
from .search_total import SearchTotal
from .search_total_relation import SearchTotalRelation
from .segment import Segment
from .segment_hit import SegmentHit
from .segment_hits import SegmentHits
from .segment_metadata import SegmentMetadata
from .segmenter import Segmenter
from .segmenter_parameters import SegmenterParameters
from .share_mode import ShareMode
from .sherpa_job_bean import SherpaJobBean
from .sherpa_job_bean_status import SherpaJobBeanStatus
from .sherpa_job_bean_type import SherpaJobBeanType
from .simple_metadata import SimpleMetadata
from .suggester import Suggester
from .suggester_parameters import SuggesterParameters
from .suggester_patch import SuggesterPatch
from .suggester_patch_parameters import SuggesterPatchParameters
from .suggestion_facets import SuggestionFacets
from .term_hit import TermHit
from .term_hit_term import TermHitTerm
from .term_hits import TermHits
from .term_identifier import TermIdentifier
from .term_import import TermImport
from .term_importer_spec import TermImporterSpec
from .term_importer_spec_parameters import TermImporterSpecParameters
from .text_count import TextCount
from .upload_files_multipart_data import UploadFilesMultipartData
from .uploaded_file import UploadedFile
from .uploaded_file_info import UploadedFileInfo
from .user_permissions_update import UserPermissionsUpdate
from .user_profile import UserProfile
from .user_profile_update import UserProfileUpdate
from .user_response import UserResponse
from .with_annotator import WithAnnotator
from .with_annotator_condition import WithAnnotatorCondition
from .with_annotator_parameters import WithAnnotatorParameters
from .with_converter import WithConverter
from .with_converter_condition import WithConverterCondition
from .with_converter_parameters import WithConverterParameters
from .with_language_guesser import WithLanguageGuesser
from .with_language_guesser_condition import WithLanguageGuesserCondition
from .with_language_guesser_parameters import WithLanguageGuesserParameters
from .with_processor import WithProcessor
from .with_processor_condition import WithProcessorCondition
from .with_processor_parameters import WithProcessorParameters
from .with_segmenter import WithSegmenter
from .with_segmenter_condition import WithSegmenterCondition
from .with_segmenter_parameters import WithSegmenterParameters

__all__ = (
    "Ack",
    "Aggregation",
    "AltText",
    "AnnotateBinaryForm",
    "AnnotateBinaryWithProjectAnnotatorMultipartData",
    "AnnotateBinaryWithProjectMultipartData",
    "AnnotatedDocAltText",
    "AnnotatedDocAnnotation",
    "AnnotatedDocAnnotationCreationMode",
    "AnnotatedDocAnnotationProperties",
    "AnnotatedDocCategory",
    "AnnotatedDocCategoryCreationMode",
    "AnnotatedDocCategoryProperties",
    "AnnotatedDocSentence",
    "AnnotatedDocSentenceMetadata",
    "AnnotatedDocument",
    "AnnotatedDocumentMetadata",
    "AnnotateDocumentsWithPipeline",
    "AnnotateFormatBinaryWithProjectAnnotatorMultipartData",
    "AnnotateTextWithPipeline",
    "Annotation",
    "AnnotationCreationMode",
    "AnnotationFacets",
    "AnnotationId",
    "AnnotationMetrics",
    "AnnotationPatch",
    "AnnotationPatchStatus",
    "AnnotationPlan",
    "AnnotationStatus",
    "AnnotationTerm",
    "AnnotationTermProperties",
    "Annotator",
    "AnnotatorMultimap",
    "ApplyTo",
    "BearerToken",
    "Bucket",
    "CategoriesFacets",
    "Category",
    "CategoryAction",
    "CategoryCreationMode",
    "CategoryId",
    "CategoryMetrics",
    "CategoryPatch",
    "CategoryPatchStatus",
    "CategoryStatus",
    "ClassificationConfig",
    "ClassificationOptions",
    "ConfigPatchOptions",
    "ConvertAnnotationPlan",
    "Converter",
    "ConverterParameters",
    "ConvertFormatAnnotationPlan",
    "CorpusMetrics",
    "CreatedByCount",
    "CreateLexiconResponse200",
    "CreateProjectFromArchiveMultipartData",
    "CreateTermJsonBody",
    "CreateTermResponse200",
    "Credentials",
    "DeleteGroupResult",
    "DeleteManyResponse",
    "DeleteResponse",
    "DependsOn",
    "DeprecatedAnnotateBinaryWithPlanRefMultipartData",
    "DeprecatedAnnotateFormatBinaryWithPlanRefMultipartData",
    "DocAltText",
    "DocAnnotation",
    "DocAnnotationCreationMode",
    "DocAnnotationProperties",
    "DocAnnotationStatus",
    "DocCategory",
    "DocCategoryCreationMode",
    "DocCategoryProperties",
    "DocCategoryStatus",
    "DocSentence",
    "DocSentenceMetadata",
    "Document",
    "DocumentFacets",
    "DocumentHit",
    "DocumentHits",
    "DocumentMetadata",
    "EngineConfig",
    "EngineConfigImportSummary",
    "EngineName",
    "Error",
    "Experiment",
    "ExperimentParameters",
    "ExperimentPatch",
    "ExperimentPatchParameters",
    "ExternalDatabases",
    "ExternalResources",
    "FormatBinaryForm",
    "FormatDocumentsWithMany",
    "Formatter",
    "FormatterParameters",
    "FormatTextWithMany",
    "Gazetteer",
    "GazetteerParameters",
    "GazetteerPatch",
    "GazetteerPatchParameters",
    "GroupDesc",
    "GroupName",
    "GroupPatch",
    "GroupShare",
    "HttpServiceMetadata",
    "HttpServiceMetadataOperations",
    "HttpServiceRecord",
    "ImportArchiveMultipartData",
    "ImportModelsMultipartData",
    "InputDocument",
    "InputDocumentMetadata",
    "ItemCount",
    "ItemRef",
    "Label",
    "LabelCount",
    "LabelNames",
    "LabelSet",
    "LabelSetUpdate",
    "LabelUpdate",
    "LaunchDocumentImportMultipartData",
    "LaunchDocumentImportSegmentationPolicy",
    "LaunchProjectRestorationFromBackupMultipartData",
    "LaunchUploadedDocumentImportSegmentationPolicy",
    "Lexicon",
    "LexiconUpdate",
    "MaybeCreateProjectsAndImportModelsFromArchiveMultipartData",
    "MetadataCount",
    "ModelMetrics",
    "ModelMetricsOptions",
    "ModelsMetrics",
    "NamedAnnotationPlan",
    "NewExperiment",
    "NewExperimentParameters",
    "NewGazetteer",
    "NewGazetteerParameters",
    "NewGroupDesc",
    "NewNamedAnnotationPlan",
    "NewRole",
    "NewSuggester",
    "NewSuggesterParameters",
    "NewUser",
    "NextStep",
    "OperationCount",
    "PartialLabel",
    "PartialLexicon",
    "PlanPatch",
    "ProjectAnnotators",
    "ProjectBean",
    "ProjectConfigCreation",
    "ProjectConfigCreationProperties",
    "ProjectOpenSession",
    "ProjectOpenSessionState",
    "ProjectProperty",
    "ProjectsAnnotators",
    "ProjectStatus",
    "QualityFigures",
    "Report",
    "ReportClasses",
    "RequestJwtTokenProjectAccessMode",
    "RoleDesc",
    "RoleUpdate",
    "SearchTotal",
    "SearchTotalRelation",
    "Segment",
    "Segmenter",
    "SegmenterParameters",
    "SegmentHit",
    "SegmentHits",
    "SegmentMetadata",
    "ShareMode",
    "SherpaJobBean",
    "SherpaJobBeanStatus",
    "SherpaJobBeanType",
    "SimpleMetadata",
    "Suggester",
    "SuggesterParameters",
    "SuggesterPatch",
    "SuggesterPatchParameters",
    "SuggestionFacets",
    "TermHit",
    "TermHits",
    "TermHitTerm",
    "TermIdentifier",
    "TermImport",
    "TermImporterSpec",
    "TermImporterSpecParameters",
    "TextCount",
    "UploadedFile",
    "UploadedFileInfo",
    "UploadFilesMultipartData",
    "UserPermissionsUpdate",
    "UserProfile",
    "UserProfileUpdate",
    "UserResponse",
    "WithAnnotator",
    "WithAnnotatorCondition",
    "WithAnnotatorParameters",
    "WithConverter",
    "WithConverterCondition",
    "WithConverterParameters",
    "WithLanguageGuesser",
    "WithLanguageGuesserCondition",
    "WithLanguageGuesserParameters",
    "WithProcessor",
    "WithProcessorCondition",
    "WithProcessorParameters",
    "WithSegmenter",
    "WithSegmenterCondition",
    "WithSegmenterParameters",
)
