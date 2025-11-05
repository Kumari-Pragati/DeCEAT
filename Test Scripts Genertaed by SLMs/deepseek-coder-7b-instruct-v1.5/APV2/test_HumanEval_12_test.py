You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_12_code import longest
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_12_code import longest

class TestLongest(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_string(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_strings(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'a')
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_same_length_strings(self):
        self.assertEqual(longest(['aaa', 'bb', 'ccc']), 'aaa')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the following scenarios:

1. An empty list: The function should return None.
2. A list with a single string: The function should return that string.
3. A list with multiple strings of different lengths: The function should return the string with the maximum length.
4. A list with multiple strings of the same length: The function should return the first string in the list.

Please note that the `HumanEval_12_code` module should contain the `longest` function for these tests to work.