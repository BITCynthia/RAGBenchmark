from typing import Dict
from abc import ABC, abstractmethod

class BaseContext(ABC):
    """
    Abstract base class for handling context data.

    Attributes:
    _text (str): The text content of the context.

    Methods:
    _extract(context_dict: Dict): Abstract method to extract information from a context dictionary, must be implemented by subclasses.
    text: Property to get the text content of the context.
    """

    def __init__(self) -> None:
        """
        Initialize the BaseContext with default values.
        """
        self._text: str = ""

    @abstractmethod
    def _extract(self, context_dict: Dict) -> None:
        """
        Abstract method to extract information from a context dictionary. This method must be implemented by any subclass.

        Parameters:
        context_dict (Dict): A dictionary containing context data from which information needs to be extracted.
        """
        pass

    @property
    def text(self) -> str:
        """
        Get the text content of the context.

        Returns:
        str: The text content of the context.
        """
        return self._text
