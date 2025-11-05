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

 import unittest
from HumanEval_12_code import longest

class TestLongestFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_element_list(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_elements_same_length(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_multiple_elements_different_lengths(self):
        self.assertEqual(longest(['a', 'bb', 'c']), 'bb')

    def test_longest_string_first(self):
        self.assertEqual(longest(['a', 'bb', 'ccc', 'dddd']), 'dddd')

    def test_empty_string(self):
        self.assertEqual(longest(['a', '', 'ccc']), 'ccc')

    def test_negative_length(self):
        self.assertEqual(longest(['-', 'a', 'bb', 'ccc']), 'ccc')

    def test_special_characters(self):
        self.assertEqual(longest(['a', 'b$', 'ccc', 'dddd!']), 'dddd!')

    def test_unicode_characters(self):
        self.assertEqual(longest(['a', 'б', 'ç', 'dddd']), 'dddd')

if __name__ == '__main__':
    unittest.main()