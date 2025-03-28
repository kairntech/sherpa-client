from enum import Enum


class NamedVectorCreationMode(str, Enum):
    MANUAL = "manual"
    AUTOMATIC = "automatic"
    UNDEFINED = "undefined"

    def __str__(self) -> str:
        return str(self.value)
