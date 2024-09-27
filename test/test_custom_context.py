import os
import sys
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ragbenchmark.context.custom_context import CustomContext, CustomRagContext

class TestCustomContext(unittest.TestCase):

    def setUp(self):
        self.context_dict = {
            "TEXT": "Sample text",
            "FILE_PATH": "path/to/file.pdf",
            "PAGE_NUMBER": [1, 2, 3]
        }
        self.custom_context = CustomContext(self.context_dict)

    def test_initialization(self):
        """Test the initialization and properties of CustomContext"""
        self.assertEqual(self.custom_context._text, self.context_dict["TEXT"])
        self.assertEqual(self.custom_context._file_path, self.context_dict["FILE_PATH"])
        self.assertEqual(self.custom_context._page_number, self.context_dict["PAGE_NUMBER"])

    def test_file_path_property(self):
        """Test the file_path property"""
        self.assertEqual(self.custom_context.file_path, "path/to/file.pdf")

    def test_page_number_property(self):
        """Test the page_number property"""
        self.assertEqual(self.custom_context.page_number, [1, 2, 3])


class TestCustomRagContext(unittest.TestCase):

    def setUp(self):
        self.context_dict = {
            "TEXT": "Sample text",
            "FILE_PATH": "path/to/file.pdf",
            "PAGE_NUMBER": [1, 2, 3],
            "SCORE": 0.85
        }
        self.custom_rag_context = CustomRagContext(self.context_dict)

    def test_initialization(self):
        """Test the initialization and properties of CustomRagContext"""
        self.assertEqual(self.custom_rag_context._text, self.context_dict["TEXT"])
        self.assertEqual(self.custom_rag_context._file_path, self.context_dict["FILE_PATH"])
        self.assertEqual(self.custom_rag_context._page_number, self.context_dict["PAGE_NUMBER"])
        self.assertEqual(self.custom_rag_context._score, self.context_dict["SCORE"])

    def test_score_property(self):
        """Test the score property"""
        self.assertEqual(self.custom_rag_context.score, 0.85)


if __name__ == '__main__':
    unittest.main()
