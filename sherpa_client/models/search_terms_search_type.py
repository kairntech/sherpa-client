from enum import Enum


class SearchTermsSearchType(str, Enum):
    VECTOR = "vector"
    TEXT = "text"
    HYBRID = "hybrid"

    def __str__(self) -> str:
        return str(self.value)
