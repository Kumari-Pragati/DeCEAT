system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


assistant

import unittest

# Importing the function to be tested
from HumanEval_28_code import concatenate

class TestConcatenate(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_single_element(self):
        self.assertEqual(concatenate(['a']), 'a')

    def test_multiple_elements(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

    def test_mixed_case(self):
        self.assertEqual(concatenate(['A', 'B', 'C']), 'ABC')

    def test_unicode_characters(self):
        self.assertEqual(concatenate(['\u00e9', '\u00e5']), '\u00e9\u00e5')

if __name__ == '__main__':
    unittest.main()


This script imports the `concatenate` function from the `HumanEval_28_code` module and defines several test cases using the `unittest.TestCase` class. Each test case uses the `assertEqual` method to verify that the output of the `concatenate` function matches the expected result. The `if __name__ == '__main__':` block ensures that the tests can be run directly when the script is executed.