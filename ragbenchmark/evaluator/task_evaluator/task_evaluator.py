import os
import sys
from typing import Optional, Dict, Tuple

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tasks.base_task import BaseTask
from chat_models.base_chat_model import BaseChatModel
from metrics.metrics_by_page_number.calc_recall_by_page_number import RecallByPageNumber
from metrics.metrics_by_page_number.calc_precision_by_page_number import PrecisionByPageNumber

class TaskEvaluator:
    def __init__(self, task: BaseTask, chat_model: Optional[BaseChatModel]):
        self.task = task
        self.chat_model = chat_model
        # metrics by page number
        self.page_number_pairs: Tuple = None
        self.recall_by_page_number: Dict[str, float] = None
        self.precision_by_page_number: Dict[str, float] = None

        self._extract_task_info()

    def _extract_task_info(self):
        self._extract_page_number_list()

    def _extract_page_number_list(self):
        baseline_page_number_list = []
        for baseline_context in self.task.baseline_contexts:
            if hasattr(baseline_context, "page_number"):
                baseline_page_number_list.append(baseline_context.page_number)

        sample_page_number_list = []
        for sample_context in self.task.sample_contexts:
            if hasattr(sample_context, "page_number"):
                sample_page_number_list.append(sample_context.page_number)

        if baseline_page_number_list and sample_page_number_list:
            self.page_number_pairs = baseline_page_number_list, sample_page_number_list

    def get_recall_by_page_number(self):
        if self.recall_by_page_number is None:
            self.recall_by_page_number = RecallByPageNumber.calculate_recall_by_page_number(self.page_number_pairs)
        return self.recall_by_page_number

    def get_precision_by_page_number(self):
        if self.precision_by_page_number is None:
            self.precision_by_page_number = PrecisionByPageNumber.calculate_precision_by_page_number(self.page_number_pairs)
        return self.precision_by_page_number

if __name__ == "__main__":
    import json
    from tasks.custom_task import CustomTask
    baseline_data_path = "data/customized_dataset/baseline.json"
    with open(baseline_data_path, "r") as f:
        baseline_dataset = json.load(f)
    sample_data_path = "data/customized_dataset/samples.json"
    with open(sample_data_path, "r") as f:
        sample_dataset = json.load(f)
    a_task = CustomTask("1", baseline_dataset["TASKS"]["1"], sample_dataset["TASKS"]["1"])

    task_evaluator = TaskEvaluator(a_task, None)
    print("recall_by_page_number", task_evaluator.get_recall_by_page_number())
    print("precision_by_page_number", task_evaluator.get_precision_by_page_number())
