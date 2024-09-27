import os
import sys
from typing import List, Dict

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from base_context import BaseContext

class CustomContext(BaseContext):
    """
    CustomContext is a class that extends BaseContext to include additional attributes
    such as file path and page numbers, extracted from a provided context dictionary.

    Attributes:
    _file_path (str): The file path associated with the context.
    _page_number (List[int]): List of page numbers relevant to the context.

    Methods:
    _extract(context_dict: Dict) -> None: Extracts required attributes from the context dictionary.
    file_path() -> str: Returns the file path.
    page_number() -> List[int]: Returns the list of page numbers.
    """

    def __init__(self, context_dict: Dict) -> None:
        """
        Initialize CustomContext with a context dictionary.

        Parameters:
        context_dict (Dict): A dictionary containing context information.
        """
        super().__init__()
        self._file_path: str = ""
        self._page_number: List[int] = []
        self._extract(context_dict)

    def _extract(self, context_dict: Dict) -> None:
        """
        Extract attributes from the context dictionary.

        Parameters:
        context_dict (Dict): A dictionary containing context information.
        """
        self._text = context_dict["TEXT"]
        self._file_path = context_dict["FILE_PATH"]
        self._page_number = context_dict["PAGE_NUMBER"]

    @property
    def file_path(self) -> str:
        """
        Get the file path associated with the context.

        Returns:
        str: The file path.
        """
        return self._file_path

    @property
    def page_number(self) -> List[int]:
        """
        Get the list of page numbers relevant to the context.

        Returns:
        List[int]: List of page numbers.
        """
        return self._page_number


class CustomRAGContext(CustomContext):
    """
    CustomRAGContext is a class that extends CustomContext to include an additional
    attribute for score, extracted from a provided context dictionary.

    Attributes:
    _score (float): The score associated with the context.

    Methods:
    _extract(context_dict: Dict) -> None: Extracts required attributes from the context dictionary.
    score() -> float: Returns the score.
    """

    def __init__(self, context_dict: Dict) -> None:
        """
        Initialize CustomRAGContext with a context dictionary.

        Parameters:
        context_dict (Dict): A dictionary containing context information.
        """
        self._score: float = 0.0
        super().__init__(context_dict)

    def _extract(self, context_dict: Dict) -> None:
        """
        Extract attributes from the context dictionary.

        Parameters:
        context_dict (Dict): A dictionary containing context information.
        """
        super()._extract(context_dict)
        self._score = context_dict["SCORE"]

    @property
    def score(self) -> float:
        """
        Get the score associated with the context.

        Returns:
        float: The score.
        """
        return self._score


if __name__ == "__main__":
    context_dict = {
        "TEXT": "Positional encoding provides information about the position of words in a sentence, which is crucial since the Transformer model does not use recurrence.",
        "FILE_PATH": "data/attention_is_all_you_need.pdf",
        "PAGE_NUMBER": [5],
        "SCORE": 0.91
    }

    custom_rag_context = CustomRAGContext(context_dict)

    print("Text:", custom_rag_context.text)
    print("File Path:", custom_rag_context.file_path)
    print("Page Number:", custom_rag_context.page_number)
    print("Score:", custom_rag_context.score)
