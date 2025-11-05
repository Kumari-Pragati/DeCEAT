You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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

    def test_single_string(self):
        self.assertEqual(longest(['a']), 'a')

    def test_multiple_strings_same_length(self):
        self.assertEqual(longest(['a', 'bb', 'ccc']), 'ccc')

    def test_multiple_strings_different_lengths(self):
        self.assertEqual(longest(['a', 'bb', 'cccc']), 'cccc')

    def test_longest_string_first(self):
        self.assertEqual(longest(['aa', 'bbb', 'ccccc']), 'ccccc')

    def test_shortest_string_first(self):
        self.assertEqual(longest(['a', 'bbbb', 'cccccc']), 'bbbb')

    def test_empty_string(self):
        self.assertEqual(longest(['a', '', 'ccccc']), 'ccccc')

    def test_non_string_elements(self):
        with self.assertRaises(TypeError):
            longest(['a', 123, 'ccccc'])

if __name__ == '__main__':
    unittest.main()