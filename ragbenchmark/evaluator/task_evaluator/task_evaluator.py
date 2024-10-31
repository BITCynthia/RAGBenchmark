import os
import sys
import warnings
from typing import Optional, Dict, Tuple

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from tasks.base_task import BaseTask
from chat_models.base_chat_model import BaseChatModel
from metrics.metrics_by_page_number.calc_recall_by_page_number import RecallByPageNumber
from metrics.metrics_by_page_number.calc_precision_by_page_number import PrecisionByPageNumber
from metrics.metrics_by_char.utils import count_chars
from metrics.metrics_by_char.calc_recall_by_char import RecallByChar
from metrics.metrics_by_char.calc_precision_by_char import PrecisionByRecall

class TaskEvaluator:
    def __init__(self, task: BaseTask, chat_model: Optional[BaseChatModel]):
        self.task = task
        self.chat_model = chat_model
        # metrics by page number
        self.page_number_pairs: Tuple = None
        self.recall_by_page_number: Dict[str, float] = None
        self.precision_by_page_number: Dict[str, float] = None
        # metrics by content
        self.text_pairs: Tuple =None
        # metrics by token
        self.token_pairs: Tuple =None
        # metrics by char
        self.char_pairs:Tuple = None
        self.recall_by_char: Dict[str, float] = None
        self.precision_by_char: Dict[str, float] = None

        self._extract_task_info()

    def _extract_task_info(self):
        self._extract_page_number_list()
        self._extract_text_list()
        self._extract_char_list()

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

    def _extract_text_list(self):
        baseline_text_list = [baseline_context.text for baseline_context in self.task.baseline_contexts]
        sample_text_list = [sample_context.text for sample_context in self.task.sample_contexts]
        self.text_pairs = baseline_text_list, sample_text_list

    def _extract_char_list(self):
        baseline_char_counter = [count_chars(baseline_text) for baseline_text in self.text_pairs[0]]
        sample_char_counter = [count_chars(sample_text) for sample_text in self.text_pairs[1]]
        self.char_pairs = baseline_char_counter, sample_char_counter

    def get_recall_by_page_number(self):
        if self.recall_by_page_number is None:
            if self.page_number_pairs is None:
                warnings.warn("No page numbers provided in the task.")
                self.recall_by_page_number = 0.0
            else:
                self.recall_by_page_number = RecallByPageNumber.calculate_recall_by_page_number(*self.page_number_pairs)
        return self.recall_by_page_number

    def get_precision_by_page_number(self):
        if self.precision_by_page_number is None:
            if self.page_number_pairs is None:
                warnings.warn("No page numbers provided in the task.")
                self.precision_by_page_number = 0.0
            else:
                self.precision_by_page_number = PrecisionByPageNumber.calculate_precision_by_page_number(*self.page_number_pairs)
        return self.precision_by_page_number

    def get_recall_by_char(self):
        if self.recall_by_char is None:
            recall_list = []
            for baseline_char_count in self.char_pairs[0]:
                for sample_char_count in self.char_pairs[1]:
                    recall_list.append(RecallByChar.calculate_recall_by_char(baseline_char_count, sample_char_count))
            self.recall_by_char = sum(recall_list) / len(recall_list)
        return self.recall_by_char

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
    print("recall_by_char", task_evaluator.get_recall_by_char())
