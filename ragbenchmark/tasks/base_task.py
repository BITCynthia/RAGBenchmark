import os
import sys
from typing import List, Dict, Optional, Any, Union
from abc import ABC, abstractmethod

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from context.base_context import BaseContext

class BaseTask(ABC):
    """
    Abstract base class for handling tasks that involve extracting information from contexts.

    Attributes:
    _id (Optional[Union[int, str]]): The unique identifier for the task, which can be an integer or string.
    _question (str): The question associated with the task.
    _answer (str): The answer associated with the task.
    _contexts (List[BaseContext]): A list of contexts.

    Methods:
    _extract(): Abstract method to extract information, must be implemented by subclasses.
    _extract_contexts(): Abstract method to extract contexts, must be implemented by subclasses.
    id: Property to get the task's unique identifier.
    question: Property to get the task's question.
    context: Property to get the task's contexts.
    """

    def __init__(self) -> None:
        """
        Initialize the BaseTask with default values.
        """
        self._id: Optional[Union[int, str]] = None
        self._question: str = ""
        self._answer: str = ""
        self._contexts: List[BaseContext] = []

    @abstractmethod
    def _extract(self, task_dict: Dict[str, Any]) -> None:
        """
        Abstract method to extract information. This method must be implemented by any subclass.
        """
        pass

    @abstractmethod
    def _extract_contexts(self, context_dicts: List[Dict[str, Any]]) -> None:
        """
        Abstract method to extract contexts. This method must be implemented by any subclass.
        """
        pass

    @property
    def id(self) -> Optional[Union[int, str]]:
        """
        Get the unique identifier for the task.

        Returns:
        Optional[Union[int, str]]: The unique identifier for the task, which can be an integer or string.
        """
        return self._id

    @property
    def question(self) -> str:
        """
        Get the question associated with the task.

        Returns:
        str: The question associated with the task.
        """
        return self._question

    @property
    def answer(self) -> str:
        """
        Get the answer associated with the task.

        Returns:
        str: The answer associated with the task.
        """
        return self._answer

    @property
    def contexts(self) -> List[BaseContext]:
        """
        Get the contexts associated with the task.

        Returns:
        List[BaseContext]: A list of contexts.
        """
        return self._contexts