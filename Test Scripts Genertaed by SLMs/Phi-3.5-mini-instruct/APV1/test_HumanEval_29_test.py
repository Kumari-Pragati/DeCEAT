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

 import unittest
from HumanEval_29_code import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_filter_with_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_no_matching_prefix(self):
        self.assertEqual(filter_by_prefix(['xyz', 'bcd', 'cde', 'array'], 'a'), [])

    def test_case_insensitive_filter(self):
        self.assertEqual(filter_by_prefix(['Abc', 'Bcd', 'Cde', 'array'], 'a'), ['Abc', 'array'])

    def test_single_element_list(self):
        self.assertEqual(filter_by_prefix(['abc'], 'a'), ['abc'])

    def test_multiple_elements_with_prefix(self):
        self.assertEqual(filter_by_prefix(['apple', 'Apple', 'banana', 'Banana'], 'a'), ['apple', 'Apple', 'banana', 'Banana'])

    def test_multiple_elements_without_prefix(self):
        self.assertEqual(filter_by_prefix(['apple', 'banana', 'cherry'], 'b'), [])

    def test_prefix_at_end_of_string(self):
        self.assertEqual(filter_by_prefix(['abcdef', 'ghijkl', 'mnopqr'], 'r'), ['mnopqr'])

    def test_prefix_with_leading_space(self):
        self.assertEqual(filter_by_prefix([' abc', ' bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_prefix_with_trailing_space(self):
        self.assertEqual(filter_by_prefix(['abc ', 'bcd', 'cde', 'array'], 'a'), ['abc '])

    def test_prefix_with_mixed_spaces(self):
        self.assertEqual(filter_by_prefix(['abc  ', 'bcd', 'cde', 'array'], 'a'), ['abc  '])

    def test_case_insensitive_filter_with_mixed_cases(self):
        self.assertEqual(filter_by_prefix(['Abc', 'bcd', 'Cde', 'array'], 'a'), ['Abc', 'array'])

    def test_empty_prefix(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], ''), ['abc', 'bcd', 'cde', 'array'])

    def test_prefix_with_non_string_type(self):
        self.assertRaises(TypeError, filter_by_prefix, ['abc', 'bcd', 'cde', 'array'], 123)

if __name__ == '__main__':
    unittest.main()