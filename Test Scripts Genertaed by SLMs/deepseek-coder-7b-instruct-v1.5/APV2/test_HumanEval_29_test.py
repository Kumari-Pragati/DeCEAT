You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a unittest test suite for the provided Python function:


import unittest
from HumanEval_29_code import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_no_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'z'), [])

    def test_single_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_multiple_prefixes(self):
        self.assertEqual(filter_by_prefix(['abc', 'abcd', 'bcd', 'cde', 'array'], 'ab'), ['abc', 'abcd'])

    def test_case_sensitivity(self):
        self.assertEqual(filter_by_prefix(['Abc', 'bcd', 'Cde', 'array'], 'a'), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for empty lists, lists with no matching prefix, lists with a single matching prefix, lists with multiple matching prefixes, and case sensitivity.