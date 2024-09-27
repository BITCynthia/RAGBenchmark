import os
import sys
from typing import List, Dict, Any

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from base_task import BaseTask
from context.custom_context import CustomContext, CustomRagContext

class CustomTask(BaseTask):
    """
    Custom task class for handling specific tasks with custom contexts.

    Attributes:
    Inherits all attributes from BaseTask.

    Methods:
    Inherits all methods from BaseTask.
    """

    def __init__(self, task_dict: Dict[str, Any]) -> None:
        """
        Initialize the CustomTask with a task dictionary.

        Args:
        task_dict (Dict[str, Any]): The dictionary containing task information.
        """
        super().__init__()
        self._extract(task_dict)

    def _extract(self, task_dict: Dict[str, Any]) -> None:
        """
        Extract information from the task dictionary.

        Args:
        task_dict (Dict[str, Any]): The dictionary containing task information.
        """
        self._id = next(iter(task_dict))
        task_info = task_dict[self._id]
        self._question = task_info["QUESTION"]
        self._answer = task_info["ANSWER"]
        self._extract_contexts(task_info["CONTEXTS"])

    def _extract_contexts(self, context_dicts: List[Dict[str, Any]]) -> None:
        """
        Extract contexts from the context dictionaries.

        Args:
        context_dicts (List[Dict[str, Any]]): The list of context dictionaries.
        """
        self._contexts = [CustomContext(context_dict) for context_dict in context_dicts]

class CustomRagTask(CustomTask):
    """
    Custom RAG task class for handling specific tasks with custom RAG contexts.

    Attributes:
    Inherits all attributes from CustomTask.

    Methods:
    Inherits all methods from CustomTask.
    """

    def __init__(self, task_dict: Dict[str, Any]) -> None:
        """
        Initialize the CustomRagTask with a task dictionary.

        Args:
        task_dict (Dict[str, Any]): The dictionary containing task information.
        """
        super().__init__(task_dict)

    def _extract_contexts(self, context_dicts: List[Dict[str, Any]]) -> None:
        """
        Extract contexts from the context dictionaries.

        Args:
        context_dicts (List[Dict[str, Any]]): The list of context dictionaries.
        """
        self._contexts = [CustomRagContext(context_dict) for context_dict in context_dicts]


if __name__ == "__main__":
    import json
    file_path = "data/customized_dataset/samples.json"
    with open(file=file_path, mode='r', encoding='utf-8') as f:
        ds_dict = json.load(f)
    tasks = ds_dict["TASKS"]

    task_id = next(iter(tasks))
    a_task = CustomRagTask({task_id: tasks[task_id]})

    print("task id:", a_task.id)
    print("question:", a_task.question)
    print("answer:", a_task.answer)
    print("contexts: *", len(a_task.contexts))