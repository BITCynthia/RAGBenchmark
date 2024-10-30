import os
import sys
from typing import Optional, List, Dict, Any
from abc import ABC, abstractmethod

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tasks.base_task import BaseTask

class BaseDataset(ABC):
    """
    Abstract base class for datasets. This class provides a template for dataset handling,
    including extraction of dataset information and tasks.

    Attributes:
    _dataset_name (Optional[str]): Name of the dataset.
    _documents (List[str]): List of documents in the dataset.
    _tasks (List[BaseTask]): List of tasks associated with the dataset.
    """

    def __init__(self) -> None:
        """
        Initializes the BaseDataset with default values.
        """
        self._dataset_name: Optional[str] = None
        self._documents: List[str] = []
        self._tasks: List[BaseTask] = []

    @abstractmethod
    def _extract(self, dataset_dict: Dict[str, Any]) -> None:
        """
        Abstract method to extract dataset information from a dictionary.

        Parameters:
        dataset_dict (Dict[str, Any]): Dictionary containing dataset information.
        """
        pass

    @abstractmethod
    def _extract_tasks(self, dataset_dict: Dict[str, Any]) -> None:
        """
        Abstract method to extract tasks from the dataset dictionary.

        Parameters:
        dataset_dict (Dict[str, Any]): Dictionary containing dataset information.
        """
        pass

    @property
    def dataset_name(self) -> Optional[str]:
        """
        Returns the name of the dataset.

        Returns:
        Optional[str]: The name of the dataset, or None if not set.
        """
        return self._dataset_name

    @property
    def documents(self) -> List[str]:
        """
        Returns the list of documents in the dataset.

        Returns:
        List[str]: A list of document strings.
        """
        return self._documents

    @property
    def tasks(self) -> List[BaseTask]:
        """
        Returns the list of tasks associated with the dataset.

        Returns:
        List[BaseTask]: A list of tasks.
        """
        return self._tasks
