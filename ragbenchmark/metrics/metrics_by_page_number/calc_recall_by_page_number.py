from typing import List

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
