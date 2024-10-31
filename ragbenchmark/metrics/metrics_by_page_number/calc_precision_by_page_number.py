import warnings
from typing import List, Tuple

class PrecisionByPageNumber:
    """
    A class used to calculate the precision of page numbers in a sample compared to a baseline.
    """

    @staticmethod
    def calculate_precision_by_page_number(
        page_number_pairs: Tuple[List[List[int]], List[List[int]]]
    ) -> float:
        """
        Calculate the precision of page numbers in the sample compared to the baseline.

        Precision is defined as the number of correctly identified page numbers (hits) divided by 
        the total number of page numbers in the sample. For each sample page number list, the 
        precision is calculated and then averaged across all sample page number lists.

        This function handles cases where the page number pairs might be None and issues a warning
        in such cases.

        Parameters:
        page_number_pairs (Tuple[List[List[int]], List[List[int]]]): A tuple containing two lists of 
                                                                    lists of page numbers. The first 
                                                                    element is the baseline page 
                                                                    number list and the second element 
                                                                    is the sample page number list.

        Returns:
        float: The average precision of the sample page numbers compared to the baseline. This is 
               a value between 0.0 and 1.0, where 1.0 means perfect precision. If the page number 
               pairs are None, a warning is issued and the precision is set to 0.0.

        Example:
        >>> page_number_pairs = ([[1, 2, 3], [4, 5, 6]], [[1, 2], [4, 5, 7]])
        >>> PrecisionByPageNumber.calculate_precision_by_page_number(page_number_pairs)
        0.8333333333333333
        """
        if page_number_pairs is None:
            warnings.warn("The task does not provide page numbers. Precision is set to 0.0.")
            return 0.0

        baseline_page_number_list, sample_page_number_list = page_number_pairs

        precision_list = []

        for sample_page_number in sample_page_number_list:
            actual_pages = len(sample_page_number)
            if actual_pages == 0:
                raise ValueError("Invalid sample page number! Page number list cannot be empty!")

            hit_pages = 0
            for baseline_page_number in baseline_page_number_list:
                hit_pages = max(hit_pages, len(set(sample_page_number) & set(baseline_page_number)))

            precision_list.append(hit_pages / actual_pages)

        return sum(precision_list) / len(precision_list) if precision_list else 0.0
