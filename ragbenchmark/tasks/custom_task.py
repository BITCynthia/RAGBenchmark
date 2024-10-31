import os
import sys
from typing import Dict, Any, Union, List

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from base_task import BaseTask
from context.custom_context import CustomContext, CustomRagContext

class CustomTask(BaseTask):
    """
    Custom task class for handling specific tasks with custom contexts.

    Attributes:
    _task_id (str): The unique identifier for the custom task.

    Methods:
    - _extract_question: Method to extract the question from the task dictionaries.
    - _extract_answer: Method to extract the answer from the task dictionary.
    - _extract_baseline_contexts: Method to extract baseline contexts from the context dictionary.
    - _extract_sample_contexts: Method to extract sample contexts from the context dictionary.
    - task_id: Property to get the unique identifier for the custom task.
    """

    def __init__(self, task_id: str, baseline_task_dict: Dict[str, Any], sample_task_dict: Dict[str, Any]) -> None:
        """
        Initialize the CustomTask with a unique identifier and task dictionaries.

        Parameters:
        task_id (str): The unique identifier for the task.
        baseline_task_dict (Dict[str, Any]): The dictionary containing baseline task information.
        sample_task_dict (Dict[str, Any]): The dictionary containing sample task information.
        """
        super().__init__()
        self._task_id = task_id
        self._question = self._extract_question(baseline_task_dict, sample_task_dict)
        self._baseline_answer = self._extract_answer(baseline_task_dict)
        self._baseline_contexts = self._extract_baseline_contexts(baseline_task_dict["CONTEXTS"])
        self._sample_answer = self._extract_answer(sample_task_dict)
        self._sample_contexts = self._extract_sample_contexts(sample_task_dict["CONTEXTS"])

    def _extract_question(self, baseline_task_dict: Dict[str, Any], sample_task_dict: Dict[str, Any]) -> str:
        """
        Extract the question from the task dictionaries.

        Parameters:
        baseline_task_dict (Dict[str, Any]): The dictionary containing baseline task information.
        sample_task_dict (Dict[str, Any]): The dictionary containing sample task information.

        Returns:
        str: The question associated with the task.

        Raises:
        AssertionError: If the questions in the baseline and sample task dictionaries do not match.
        """
        assert baseline_task_dict["QUESTION"] == sample_task_dict["QUESTION"], "Questions of baseline and sample do not belong to one task!"
        return baseline_task_dict["QUESTION"]

    def _extract_answer(self, task_dict: Dict[str, Any]) -> str:
        """
        Extract the answer from the task dictionary.

        Parameters:
        task_dict (Dict[str, Any]): The dictionary containing task information.

        Returns:
        str: The answer associated with the task.
        """
        return task_dict["ANSWER"]

    def _extract_baseline_contexts(self, baseline_context_dict: List[Dict[str, Any]]) -> List[CustomContext]:
        """
        Extract baseline contexts from the context dictionary.

        Parameters:
        baseline_context_dict (List[Dict[str, Any]]): The list of dictionaries containing baseline context information.

        Returns:
        List[CustomContext]: A list of CustomContext objects.
        """
        return [CustomContext(context_dict) for context_dict in baseline_context_dict]

    def _extract_sample_contexts(self, sample_context_dict: List[Dict[str, Any]]) -> List[CustomRagContext]:
        """
        Extract sample contexts from the context dictionary.

        Parameters:
        sample_context_dict (List[Dict[str, Any]]): The list of dictionaries containing sample context information.

        Returns:
        List[CustomRagContext]: A list of CustomRagContext objects.
        """
        return [CustomRagContext(context_dict) for context_dict in sample_context_dict]

    @property
    def task_id(self) -> Union[int, str]:
        """
        Get the unique identifier for the task.

        Returns:
        Union[int, str]: The unique identifier for the task, which can be an integer or string.
        """
        return self._task_id

if __name__ == "__main__":
    import json
    baseline_data_path = "data/customized_dataset/baseline.json"
    with open(baseline_data_path, "r") as f:
        baseline_dataset = json.load(f)
    sample_data_path = "data/customized_dataset/samples.json"
    with open(sample_data_path, "r") as f:
        sample_dataset = json.load(f)

    a_task = CustomTask("1", baseline_dataset["TASKS"]["1"], sample_dataset["TASKS"]["1"])
    print("task id:", a_task.task_id)
    print("question:", a_task.question)
    print("baseline answer:", a_task.baseline_answer)
    print("baseline contexts: *", len(a_task.baseline_contexts))
    print("sample answer:", a_task.sample_answer)
    print("sample contexts: *", len(a_task.sample_contexts))