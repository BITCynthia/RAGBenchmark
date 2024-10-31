import os
import sys
from typing import List, Any
from abc import ABC, abstractmethod

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from context.base_context import BaseContext

class BaseTask(ABC):
    """
    Abstract base class for handling tasks that involve extracting information from contexts.

    Attributes:
    _question (str): The question associated with the task.
    _baseline_answer (str): The baseline answer associated with the task.
    _baseline_contexts (List[BaseContext]): A list of baseline contexts.
    _sample_answer (str): The sample answer associated with the task.
    _sample_contexts (List[BaseContext]): A list of sample contexts.

    Methods:
    question: Property to get the task's question.
    baseline_answer: Property to get the task's baseline answer.
    baseline_contexts: Property to get the task's baseline contexts.
    sample_answer: Property to get the task's sample answer.
    sample_contexts: Property to get the task's sample contexts.
    """

    def __init__(self) -> None:
        """
        Initialize the BaseTask with default values.
        """
        self._question: str = ""
        self._baseline_answer: str = ""
        self._baseline_contexts: List[BaseContext] = []
        self._sample_answer: str = ""
        self._sample_contexts: List[BaseContext] = []

    @property
    def question(self) -> str:
        """
        Get the question associated with the task.

        Returns:
        str: The question associated with the task.
        """
        return self._question

    @property
    def baseline_answer(self) -> str:
        """
        Get the baseline answer associated with the task.

        Returns:
        str: The baseline answer associated with the task.
        """
        return self._baseline_answer

    @property
    def baseline_contexts(self) -> List[BaseContext]:
        """
        Get the baseline contexts associated with the task.

        Returns:
        List[BaseContext]: A list of baseline contexts.
        """
        return self._baseline_contexts

    @property
    def sample_answer(self) -> str:
        """
        Get the sample answer associated with the task.

        Returns:
        str: The sample answer associated with the task.
        """
        return self._sample_answer

    @property
    def sample_contexts(self) -> List[BaseContext]:
        """
        Get the sample contexts associated with the task.

        Returns:
        List[BaseContext]: A list of sample contexts.
        """
        return self._sample_contexts
