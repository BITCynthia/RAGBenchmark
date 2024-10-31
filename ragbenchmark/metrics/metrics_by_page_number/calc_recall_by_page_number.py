import os
import sys
import warnings
from typing import List, Tuple

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class RecallByPageNumber:
    """
    A class used to calculate the recall of page numbers in a sample compared to a baseline.
    """

    @staticmethod
    def calculate_recall_by_page_number(
        page_number_pairs: Tuple[List[List[int]], List[List[int]]]
    ) -> float:
        """
        Calculate the recall of page numbers in the sample compared to the baseline.

        Recall is defined as the number of correctly identified page numbers (hits) divided by 
        the total number of page numbers in the baseline. For each baseline page number list, the 
        recall is calculated and then averaged across all baseline page number lists.

        This function handles cases where the page number pairs might be None and issues a warning
        in such cases.

        Parameters:
        page_number_pairs (Tuple[List[List[int]], List[List[int]]]): A tuple containing two lists of 
                                                                    lists of page numbers. The first 
                                                                    element is the baseline page 
                                                                    number list and the second element 
                                                                    is the sample page number list.

        Returns:
        float: The average recall of the sample page numbers compared to the baseline. This is 
               a value between 0.0 and 1.0, where 1.0 means perfect recall. If the page number 
               pairs are None, a warning is issued and the recall is set to 0.0.

        Example:
        >>> page_number_pairs = ([[1, 2, 3], [4, 5, 6]], [[1, 2], [4, 5, 7]])
        >>> RecallByPageNumber.calculate_recall_by_page_number(page_number_pairs)
        0.8333333333333333
        """
        if page_number_pairs is None:
            warnings.warn("The task does not provide page numbers. Recall is set to 0.0.")
            return 0.0

        baseline_page_number_list, sample_page_number_list = page_number_pairs

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
