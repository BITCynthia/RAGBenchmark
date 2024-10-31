from typing import List

class PrecisionByPageNumber:
    """
    A class used to calculate the precision of page numbers in a sample compared to a baseline.
    """

    @staticmethod
    def calculate_precision_by_page_number(
        baseline_page_number_list: List[List[int]],
        sample_page_number_list: List[List[int]]
    ) -> float:
        """
        Calculate the precision of page numbers in the sample compared to the baseline.

        Precision is defined as the number of correctly identified page numbers (hits) divided by 
        the total number of page numbers in the sample. For each sample page number list, the 
        precision is calculated and then averaged across all sample page number lists.

        Parameters:
        baseline_page_number_list (List[List[int]]): A list of lists where each inner list contains 
                                                     page numbers from the baseline.
        sample_page_number_list (List[List[int]]): A list of lists where each inner list contains 
                                                   page numbers from the sample.

        Returns:
        float: The average precision of the sample page numbers compared to the baseline. This is 
               a value between 0.0 and 1.0, where 1.0 means perfect precision.

        Example:
        >>> baseline = [[1, 2, 3], [4, 5, 6]]
        >>> sample = [[1, 2], [4, 5, 7]]
        >>> PrecisionByRecall.calculate_precision_by_page_number(baseline, sample)
        0.8333333333333333
        """
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
