system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Provided function
from HumanEval_29_code import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])
    
    def test_single_element(self):
        self.assertEqual(filter_by_prefix(['abc'], 'a'), ['abc'])
    
    def test_multiple_elements_with_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])
    
    def test_multiple_elements_without_prefix(self):
        self.assertEqual(filter_by_prefix(['hello', 'world', 'hi', 'there'], 'a'), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for edge cases (empty list, single element), as well as typical use cases where the function should work correctly. It also checks for scenarios where the function does not match expectations, ensuring robust coverage.