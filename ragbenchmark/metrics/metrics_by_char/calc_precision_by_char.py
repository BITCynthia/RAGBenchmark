from typing import Dict

class PrecisionByRecall:
    """
    A class used to calculate the precision of characters in a sample compared to a baseline.
    """

    @staticmethod
    def calculate_precision_by_char(
        baseline_char_count: Dict[str, int],
        sample_char_count: Dict[str, int]
    ) -> float:
        """
        Calculate the precision of characters in the sample compared to the baseline.

        Precision is defined as the number of correctly identified characters (hits) divided by 
        the total number of characters in the sample. A hit is counted when a character in the 
        sample matches a character in the baseline, and the minimum count of that character in 
        both the sample and baseline is taken as the number of hits for that character.

        Parameters:
        baseline_char_count (Dict[str, int]): A dictionary where keys are characters and values 
                                              are their counts in the baseline text.
        sample_char_count (Dict[str, int]): A dictionary where keys are characters and values 
                                            are their counts in the sample text.

        Returns:
        float: The precision of the sample text compared to the baseline. This is a value between 
               0.0 and 1.0, where 1.0 means perfect precision.

        Example:
        >>> baseline = {'a': 3, 'b': 2, 'c': 1}
        >>> sample = {'a': 2, 'b': 1, 'c': 1, 'd': 1}
        >>> PrecisionByRecall.calculate_precision_by_char(baseline, sample)
        0.8
        """
        total_chars = sum(sample_char_count.values())
        hit_count = 0

        for char, count in baseline_char_count.items():
            if char in sample_char_count:
                hit_count += min(count, sample_char_count[char])

        return hit_count / total_chars if total_chars > 0 else 0.0