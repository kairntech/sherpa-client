from enum import Enum


class GetGlobalMessagesScopeItem(str, Enum):
    CLASSIFY_QUESTION = "classify_question"
    LOGIN = "login"
    SEARCH_DOCUMENTS = "search_documents"
    SET_CHAT_PARAMETERS = "set_chat_parameters"
    SYSTEM_PROMPT = "system_prompt"

    def __str__(self) -> str:
        return str(self.value)
