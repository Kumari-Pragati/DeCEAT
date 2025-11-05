You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
Here is a unittest script for the given Python function:


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
        self.assertEqual(longest(['aaa', 'bb', 'ccc']), 'aaa')

    def test_same_length_strings(self):
        self.assertEqual(longest(['aaa', 'bb', 'ccc']), 'aaa')
        self.assertEqual(longest(['abc', 'def', 'ghi']), 'abc')

if __name__ == '__main__':
    unittest.main()


This script tests the `longest` function with different scenarios:

1. An empty list: The function should return `None`.
2. A list with a single string: The function should return that string.
3. A list with multiple strings: The function should return the first string with the maximum length.
4. A list with strings of the same length: The function should return the first string with the maximum length.

The `unittest` module is a built-in Python library for testing code. It provides a rich set of tools for constructing and running tests.