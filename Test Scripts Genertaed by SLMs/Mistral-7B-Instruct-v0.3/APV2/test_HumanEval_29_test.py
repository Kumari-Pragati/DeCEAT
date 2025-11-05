You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_29_code import filter_by_prefix
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [x for x in strings if x.startswith(prefix)]

 Here is the complete unittest test suite for the `filter_by_prefix` function:


import unittest
from HumanEval_29_code import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_no_matching_strings(self):
        self.assertEqual(filter_by_prefix(['bcd', 'cde', 'array'], 'a'), [])

    def test_single_matching_string(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc'])

    def test_multiple_matching_strings(self):
        self.assertEqual(filter_by_prefix(['abc', 'array', 'apple', 'array_list'], 'array'), ['array', 'array_list'])

    def test_case_insensitive(self):
        self.assertEqual(filter_by_prefix(['AbC', 'array', 'Apple', 'array_list'], 'a'), ['AbC', 'array'])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the following scenarios:

1. An empty list with a given prefix.
2. A list with no strings matching the given prefix.
3. A list with a single string matching the given prefix.
4. A list with multiple strings matching the given prefix.
5. A test for case-insensitivity.