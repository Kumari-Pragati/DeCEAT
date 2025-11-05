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

 Here is a simple unittest test script for the `concatenate` function:


import unittest
from HumanEval_28_code import concatenate

class TestConcatenateFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(concatenate([]), '')

    def test_single_element_list(self):
        self.assertEqual(concatenate(['a']), 'a')

    def test_multiple_elements_list(self):
        self.assertEqual(concatenate(['a', 'b', 'c']), 'abc')

    def test_list_with_spaces(self):
        self.assertEqual(concatenate(['a', ' ', 'b', ' ', 'c']), 'a b c')

    def test_list_with_special_characters(self):
        self.assertEqual(concatenate(['a', '#', 'b', '%', 'c']), 'a#b%c')

    def test_list_with_numbers(self):
        self.assertEqual(concatenate(['a', '1', 'b', '2', 'c']), 'a1b2c')

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases to ensure the `concatenate` function works as expected with different inputs. It covers empty lists, single-element lists, lists with multiple elements, lists with spaces, lists with special characters, and lists with numbers.