import os
import sys
from typing import Dict, Any

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from base_dataset import BaseDataset
from tasks.custom_task import CustomTask, CustomRagTask

class CustomDataset(BaseDataset):
    """
    A custom dataset class that extends the BaseDataset class. It initializes and extracts
    dataset information and tasks from a provided dictionary.

    Attributes:
    _dataset_name (Optional[str]): Name of the dataset.
    _documents (List[str]): List of documents in the dataset.
    _tasks (List[BaseTask]): List of tasks associated with the dataset.
    """

    def __init__(self, dataset_dict: Dict[str, Any]) -> None:
        """
        Initializes the CustomDataset and extracts dataset information and tasks.

        Parameters:
        dataset_dict (Dict[str, Any]): Dictionary containing dataset information.
        """
        super().__init__()
        self._extract(dataset_dict)

    def _extract(self, dataset_dict: Dict[str, Any]) -> None:
        """
        Extracts dataset information from the provided dictionary.

        Parameters:
        dataset_dict (Dict[str, Any]): Dictionary containing dataset information.
        """
        self._dataset_name = dataset_dict["NAME"]
        self._documents = dataset_dict["DOCUMENTS"]
        self._extract_tasks(dataset_dict["TASKS"])

    def _extract_tasks(self, tasks_dict: Dict[str, Dict[str, Any]]) -> None:
        """
        Extracts tasks from the provided dictionary and appends them to the tasks list.

        Parameters:
        tasks_dict (Dict[str, Dict[str, Any]]): Dictionary containing task information.
        """
        for task_id, task_info in tasks_dict.items():
            self._tasks.append(CustomTask({task_id: task_info}))

class CustomRagDataset(CustomDataset):
    """
    A custom RAG (Retrieval-Augmented Generation) dataset class that extends the CustomDataset class.
    It specifically handles tasks related to RAG by utilizing the CustomRagTask class.

    Attributes:
    _dataset_name (Optional[str]): Name of the dataset.
    _documents (List[str]): List of documents in the dataset.
    _tasks (List[BaseTask]): List of tasks associated with the dataset.
    """

    def __init__(self, dataset_dict: Dict[str, Any]) -> None:
        """
        Initializes the CustomRagDataset and extracts dataset information and tasks.

        Parameters:
        dataset_dict (Dict[str, Any]): Dictionary containing dataset information.
        """
        super().__init__(dataset_dict)

    def _extract_tasks(self, tasks_dict: Dict[str, Dict[str, Any]]) -> None:
        """
        Extracts RAG-specific tasks from the provided dictionary and appends them to the tasks list.

        Parameters:
        tasks_dict (Dict[str, Dict[str, Any]]): Dictionary containing task information.
        """
        for task_id, tasks_info in tasks_dict.items():
            self._tasks.append(CustomRagTask({task_id: tasks_info}))

if __name__ == "__main__":
    import json

    # Example usage for CustomDataset
    file_path = "data/customized_dataset/baseline.json"
    with open(file=file_path, mode='r', encoding='utf-8') as f:
        ds_dict = json.load(f)
    ds = CustomDataset(ds_dict)

    print("dataset name:", ds.dataset_name)
    print("documents:", ds.documents)
    print("task number:", len(ds.tasks))

    # Example usage for CustomRagDataset
    file_path = "data/customized_dataset/samples.json"
    with open(file=file_path, mode='r', encoding='utf-8') as f:
        ds_dict = json.load(f)
    ds = CustomRagDataset(ds_dict)

    print("dataset name:", ds.dataset_name)
    print("documents:", ds.documents)
    print("task number:", len(ds.tasks))
