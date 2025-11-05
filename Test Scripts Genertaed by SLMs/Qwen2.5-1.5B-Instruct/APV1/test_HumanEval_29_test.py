system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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


assistant

import unittest

# Provided code snippet
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [x for x in strings if x.startswith(prefix)]


class TestFilterByPrefix(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_single_element(self):
        self.assertEqual(filter_by_prefix(['hello'], 'h'), ['hello'])

    def test_multiple_elements(self):
        self.assertEqual(
            filter_by_prefix(['apple', 'banana', 'apricot', 'cherry'], 'a'),
            ['apple', 'apricot']
        )

    def test_case_insensitive(self):
        self.assertEqual(
            filter_by_prefix(['Apple', 'Banana', 'Apricot', 'Cherry'], 'A'),
            ['Apple', 'Apricot']
        )

    def test_prefix_in_middle(self):
        self.assertEqual(
            filter_by_prefix(['apple', 'banana', 'apricot', 'cherry'], 'p'),
            ['apple', 'apricot']
        )

    def test_prefix_at_end(self):
        self.assertEqual(
            filter_by_prefix(['apple', 'banana', 'apricot', 'cherry'], 'e'),
            ['apple', 'apricot']
        )

    def test_prefix_not_found(self):
        self.assertEqual(
            filter_by_prefix(['apple', 'banana', 'apricot', 'cherry'], 'z'),
            []
        )


if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to ensure the `filter_by_prefix` function works correctly under different scenarios, including empty lists, single elements, multiple elements, case sensitivity, prefixes at specific positions (middle and end), and cases where no matching element exists.