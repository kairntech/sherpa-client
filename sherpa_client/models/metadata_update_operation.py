from enum import Enum


class MetadataUpdateOperation(str, Enum):
    ADD_METADATA = "ADD_METADATA"
    REMOVE_METADATA = "REMOVE_METADATA"
    REMOVE_METADATA_VALUE = "REMOVE_METADATA_VALUE"
    REPLACE_METADATA_VALUE = "REPLACE_METADATA_VALUE"

    def __str__(self) -> str:
        return str(self.value)
