import os
import sys
import unittest
from unittest.mock import patch, MagicMock

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ragbenchmark.context.custom_context import CustomContext, CustomRagContext
from ragbenchmark.tasks.custom_task import CustomTask, CustomRagTask

class TestCustomTask(unittest.TestCase):
    def setUp(self):
        self.task_dict = {
            "task1": {
                "QUESTION": "What is AI?",
                "ANSWER": "Artificial Intelligence",
                "CONTEXTS": [
                    {
                        "TEXT": "AI is the simulation of human intelligence in machines.",
                        "FILE_PATH": "test.txt",
                        "PAGE_NUMBER": [1]
                        },
                    {
                        "TEXT": "AI applications include expert systems, natural language processing, and robotics.",
                        "FILE_PATH": "text.txt",
                        "PAGE_NUMBER": [3]
                        }
                ]
            }
        }

    def test_initialization(self):
        task = CustomTask(self.task_dict)
        self.assertEqual(task._id, "task1")
        self.assertEqual(task._question, "What is AI?")
        self.assertEqual(task._answer, "Artificial Intelligence")
        self.assertEqual(len(task._contexts), 2)

    @patch('ragbenchmark.context.custom_context.CustomContext')
    def test_context_extraction(self, MockCustomContext):
        MockCustomContext.side_effect = lambda x: x  # Mocking CustomContext to return the input dictionary
        task = CustomTask(self.task_dict)
        self.assertEqual(len(task._contexts), len(self.task_dict["task1"]["CONTEXTS"]))

    def test_empty_contexts(self):
        empty_context_task_dict = {
            "task1": {
                "QUESTION": "What is AI?",
                "ANSWER": "Artificial Intelligence",
                "CONTEXTS": []
            }
        }
        task = CustomTask(empty_context_task_dict)
        self.assertEqual(len(task._contexts), 0)

    def test_missing_keys(self):
        incomplete_task_dict = {
            "task1": {
                "QUESTION": "What is AI?"
                # Missing 'ANSWER' and 'CONTEXTS'
            }
        }
        with self.assertRaises(KeyError):
            CustomTask(incomplete_task_dict)

class TestCustomRagTask(unittest.TestCase):
    def setUp(self):
        self.task_dict = {
            "task1": {
                "QUESTION": "What is AI?",
                "ANSWER": "Artificial Intelligence",
                "CONTEXTS": [
                    {
                        "TEXT": "AI is the simulation of human intelligence in machines.",
                        "FILE_PATH": "test.txt",
                        "PAGE_NUMBER": [1],
                        "SCORE": 0.95
                        },
                    {
                        "TEXT": "AI applications include expert systems, natural language processing, and robotics.",
                        "FILE_PATH": "text.txt",
                        "PAGE_NUMBER": [3],
                        "SCORE": 0.90
                        }
                ]
            }
        }

    def test_initialization(self):
        task = CustomRagTask(self.task_dict)
        self.assertEqual(task._id, "task1")
        self.assertEqual(task._question, "What is AI?")
        self.assertEqual(task._answer, "Artificial Intelligence")
        self.assertEqual(len(task._contexts), 2)

    @patch('ragbenchmark.context.custom_context.CustomRagContext')
    def test_context_extraction(self, MockCustomRagContext):
        MockCustomRagContext.side_effect = lambda x: x  # Mocking CustomRagContext to return the input dictionary
        task = CustomRagTask(self.task_dict)
        self.assertEqual(len(task._contexts), len(self.task_dict["task1"]["CONTEXTS"]))

    def test_empty_contexts(self):
        empty_context_task_dict = {
            "task1": {
                "QUESTION": "What is AI?",
                "ANSWER": "Artificial Intelligence",
                "CONTEXTS": []
            }
        }
        task = CustomRagTask(empty_context_task_dict)
        self.assertEqual(len(task._contexts), 0)

    def test_missing_keys(self):
        incomplete_task_dict = {
            "task1": {
                "QUESTION": "What is AI?"
                # Missing 'ANSWER' and 'CONTEXTS'
            }
        }
        with self.assertRaises(KeyError):
            CustomRagTask(incomplete_task_dict)

if __name__ == '__main__':
    unittest.main()
