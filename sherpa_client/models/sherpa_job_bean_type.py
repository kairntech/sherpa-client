from enum import Enum


class SherpaJobBeanType(str, Enum):
    DOC_IMPORT = "DOC_IMPORT"
    EXPERIMENT_TRAINING = "EXPERIMENT_TRAINING"
    DOC_DELETION = "DOC_DELETION"
    CORPUS_ANNOTATE = "CORPUS_ANNOTATE"
    TRAIN_AND_SUGGEST = "TRAIN_AND_SUGGEST"
    UNSPECIFIED = "UNSPECIFIED"
    PROJECT_INDEXING = "PROJECT_INDEXING"
    PROJECTS_INDEXING = "PROJECTS_INDEXING"
    PROJECT_RESTORATION = "PROJECT_RESTORATION"
    DELETE_LABELS = "DELETE_LABELS"
    PROCESS_CANDIDATES = "PROCESS_CANDIDATES"
    SYNCHRONIZE_TERMS = "SYNCHRONIZE_TERMS"
    TERM_IMPORT = "TERM_IMPORT"

    def __str__(self) -> str:
        return str(self.value)
