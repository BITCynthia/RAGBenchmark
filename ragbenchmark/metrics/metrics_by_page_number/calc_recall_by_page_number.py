import os
import sys
import warnings
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tasks.base_task import BaseTask

class RecallByPageNumber:
    """
    A class used to calculate the recall of page numbers in a sample compared to a baseline.
    """

    @staticmethod
    def calculate_recall_by_page_number(
        baseline_page_number_list: List[List[int]],
        sample_page_number_list: List[List[int]]
    ) -> float:
        """
        Calculate the recall of page numbers in the sample compared to the baseline.

        Recall is defined as the number of correctly identified page numbers (hits) divided by 
        the total number of page numbers in the baseline. For each baseline page number list, the 
        recall is calculated and then averaged across all baseline page number lists.

        Parameters:
        baseline_page_number_list (List[List[int]]): A list of lists where each inner list contains 
                                                     page numbers from the baseline.
        sample_page_number_list (List[List[int]]): A list of lists where each inner list contains 
                                                   page numbers from the sample.

        Returns:
        float: The average recall of the sample page numbers compared to the baseline. This is 
               a value between 0.0 and 1.0, where 1.0 means perfect recall.

        Example:
        >>> baseline = [[1, 2, 3], [4, 5, 6]]
        >>> sample = [[1, 2], [4, 5, 7]]
        >>> RecallByPageNumber.calculate_recall_by_page_number(baseline, sample)
        0.8333333333333333
        """
        recall_list = []

        for baseline_page_number in baseline_page_number_list:
            expected_pages = len(baseline_page_number)
            if expected_pages == 0:
                raise ValueError("Invalid baseline page number! Page number list cannot be empty!")

            hit_pages = 0
            for sample_page_number in sample_page_number_list:
                hit_pages = max(hit_pages, len(set(baseline_page_number) & set(sample_page_number)))

            recall_list.append(hit_pages / expected_pages)

        return sum(recall_list) / len(recall_list) if recall_list else 0.0

    def calculate_recall_by_page_number_for_a_task(task: BaseTask) -> float:
        """
        Calculate the recall by page number for a given task.

        This function compares the baseline contexts and sample contexts of the task by their page numbers
        and calculates the recall. If no page numbers are provided, a warning is issued and the recall is set to 0.0.

        Parameters:
        task (BaseTask): The task for which recall is to be calculated. The task should have baseline contexts 
                        and sample contexts with page numbers.

        Returns:
        float: The recall by page number for the given task. Returns 0.0 if no page numbers are provided.

        Example:
        >>> task = CustomTask("1", baseline_task_dict, sample_task_dict)
        >>> recall = calculate_recall_by_page_number_for_a_task(task)
        >>> print(recall)
        0.75
        """

        baseline_page_number_list = []
        for baseline_context in task.baseline_contexts:
            if hasattr(baseline_context, "page_number"):
                baseline_page_number_list.append(baseline_context.page_number)

        sample_page_number_list = []
        for sample_context in task.sample_contexts:
            if hasattr(sample_context, "page_number"):
                sample_page_number_list.append(sample_context.page_number)

        if not baseline_page_number_list or not sample_page_number_list:
            warnings.warn("The task does not provide page numbers. Recall is set to 0.0.")
            return 0.0

        recall_by_page_number = RecallByPageNumber.calculate_recall_by_page_number(baseline_page_number_list, sample_page_number_list)
        return recall_by_page_number
