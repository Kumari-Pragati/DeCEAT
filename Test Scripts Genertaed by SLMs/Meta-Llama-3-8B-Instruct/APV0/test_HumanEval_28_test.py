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
    return ''.join(strings)assistant

Here is the unittest test script for the `concatenate` function:

import unittest
from HumanEval_28_code import concatenate

class TestConcatenate(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_single_element_list(self):
        self.assertEqual(concatenate(['a']), 'a')

    def test_multiple_elements_list(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

    def test_list_with_spaces(self):
        self.assertEqual(concatenate(['a', 'b ', 'c']), 'a b c')

    def test_list_with_newlines(self):
        self.assertEqual(concatenate(['a', 'b\n', 'c']), 'a\nb\nc')

    def test_list_with_special_chars(self):
        self.assertEqual(concatenate(['a', 'b!', 'c']), 'a b!c')

if __name__ == '__main__':
    unittest.main()

This script tests the `concatenate` function with various inputs, including:

1. An empty list
2. A list with a single element
3. A list with multiple elements
4. A list with spaces
5. A list with newlines
6. A list with special characters

Each test case uses the `assertEqual` method to verify that the output of the `concatenate` function matches the expected result.