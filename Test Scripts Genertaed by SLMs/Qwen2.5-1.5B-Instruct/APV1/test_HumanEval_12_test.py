system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function definition provided in the problem description
from HumanEval_12_code import longest

class TestLongest(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_element(self):
        self.assertEqual(longest(["a"]), "a")

    def test_multiple_elements(self):
        self.assertEqual(longest(["a", "bb", "ccc"]), "ccc")

    def test_equal_length_strings(self):
        self.assertEqual(longest(["aaa", "bbb", "ccc"]), "aaa")

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestLongest` class that inherits from `unittest.TestCase`. It contains several test methods to verify the correctness of the `longest` function under different scenarios as described in the docstring. The `assertIsNone`, `assertEquals`, and `assertTrue` methods are used to check the expected outcomes. Finally, the `unittest.main()` call at the end runs all the tests when the script is executed directly.