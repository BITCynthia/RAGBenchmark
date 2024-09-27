import os
import sys
import unittest
from typing import Dict
from abc import ABC, abstractmethod

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ragbenchmark.context.base_context import BaseContext

class ConcreteContext(BaseContext):
    def _extract(self, context_dict: Dict) -> None:
        self._text = context_dict.get("text", "")


class TestBaseContext(unittest.TestCase):
    def test_initialization(self):
        """Test that the BaseContext initializes with an empty _text attribute."""
        context = ConcreteContext()
        self.assertEqual(context._text, "")
    
    def test_abstract_method(self):
        """Test that the _extract method is abstract and must be implemented."""
        with self.assertRaises(TypeError):
            BaseContext()
    
    def test_text_property(self):
        """Test that the text property returns the correct value."""
        context = ConcreteContext()
        context._text = "Sample Text"
        self.assertEqual(context.text, "Sample Text")
    
    def test_extract_method(self):
        """Test that the extract method sets the _text attribute correctly."""
        context = ConcreteContext()
        sample_dict = {"text": "Extracted Text"}
        context._extract(sample_dict)
        self.assertEqual(context.text, "Extracted Text")
    
    def test_extract_method_no_text(self):
        """Test the extract method with a dictionary that has no 'text' key."""
        context = ConcreteContext()
        sample_dict = {"not_text": "No Text Here"}
        context._extract(sample_dict)
        self.assertEqual(context.text, "")


if __name__ == "__main__":
    unittest.main()
