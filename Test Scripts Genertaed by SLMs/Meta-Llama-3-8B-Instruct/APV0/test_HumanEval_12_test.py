user

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
            return sassistant

Here is the unittest test script for the `longest` function:

import unittest
from HumanEval_12_code import longest

class TestLongest(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_element_list(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_elements_list(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_multiple_elements_with_same_length(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'a')

    def test_list_with_no_strings(self):
        self.assertIsNone(longest(['', '']))

    def test_list_with_mixed_lengths(self):
        self.assertEqual(longest(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']), 'i')

if __name__ == '__main__':
    unittest.main()

This test script covers the following scenarios:

1. An empty list
2. A list with a single element
3. A list with multiple elements of different lengths
4. A list with multiple elements of the same length
5. A list with no strings (i.e., only empty strings)
6. A list with mixed lengths

Each test method uses the `assertIsNone`, `assertEqual`, or `assertRaises` methods to verify that the `longest` function behaves as expected.