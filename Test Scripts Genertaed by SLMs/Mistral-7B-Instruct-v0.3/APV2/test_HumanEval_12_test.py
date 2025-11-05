You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is the complete unittest test suite for the `longest` function:


import unittest
from HumanEval_12_code import longest

class TestLongest(unittest.TestCase):

    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_string(self):
        self.assertEqual(longest(['a']), 'a')
        self.assertEqual(longest(['A']), 'A')
        self.assertEqual(longest(['Z']), 'Z')

    def test_multiple_strings(self):
        self.assertEqual(longest(['a', 'b', 'c']), 'a')
        self.assertEqual(longest(['A', 'B', 'C']), 'A')
        self.assertEqual(longest(['z', 'Z', 'ZZ']), 'ZZ')

    def test_strings_of_same_length(self):
        self.assertEqual(longest(['aa', 'ab', 'ac']), 'aa')
        self.assertEqual(longest(['Aa', 'Ab', 'Ac']), 'Aa')
        self.assertEqual(longest(['zz', 'Zz', 'ZZz']), 'ZZz')

    def test_long_strings(self):
        self.assertEqual(longest(['abcdefghijklmnopqrstuvwxyz']), 'abcdefghijklmnopqrstuvwxyz')
        self.assertEqual(longest(['ABCDEFGHIJKLMNOPQRSTUVWXYZ']), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.assertEqual(longest(['12345678901234567890']), '12345678901234567890')

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for an empty list, single strings, multiple strings of different lengths, strings of the same length, and long strings. It uses the `unittest.TestCase` class to define test methods and the `unittest.main()` function to run the tests.