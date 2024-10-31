from typing import Dict

def count_chars(content: str) -> Dict[str, int]:
    """
    Count the occurrences of each character in a given string.

    Parameters:
    content (str): The string for which to count character occurrences.

    Returns:
    Dict[str, int]: A dictionary where keys are characters and values are the number of times each character appears in the input string.

    Example:
    >>> count_chars("hello")
    {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    char_count = {}
    for char in content:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
