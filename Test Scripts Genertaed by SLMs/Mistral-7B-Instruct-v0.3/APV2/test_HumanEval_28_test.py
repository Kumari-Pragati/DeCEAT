You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_28_code import concatenate
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def concatenate(strings: List[str]) -> str:
    """Concatenate list of strings into a single string.
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)

 Here is a complete unittest test suite for the `concatenate` function:


import unittest
from HumanEval_28_code import concatenate

class TestConcatenate(unittest.TestCase):

    def test_empty_list(self):
        """Test concatenating an empty list"""
        self.assertEqual(concatenate([]), '')

    def test_single_string(self):
        """Test concatenating a single string"""
        self.assertEqual(concatenate(['a']), 'a')

    def test_multiple_strings(self):
        """Test concatenating multiple strings"""
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

    def test_mixed_types(self):
        """Test concatenating a list with mixed types"""
        self.assertEqual(concatenate(['a', 1, 'b']), 'a1b')

    def test_empty_string(self):
        """Test concatenating a list with an empty string"""
        self.assertEqual(concatenate(['', 'a', 'b']), 'ab')

if __name__ == '__main__':
    unittest.main()


This test suite includes five test cases to cover various scenarios, including an empty list, a single string, multiple strings, mixed types, and a list with an empty string.