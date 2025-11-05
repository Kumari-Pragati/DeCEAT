You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_7_code import filter_by_substring
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter the list of strings and return only those that contain `substring`.
    >>> filter_by_substring(['abc', 'def', 'ab'], 'ab')
    ['abc', 'ab']
    """
    return [x for x in strings if substring in x]

 import unittest
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):

    def test_filter_by_substring_positive(self):
        strings = ['abc', 'def', 'ab']
        substring = 'ab'
        expected_output = ['abc', 'ab']
        self.assertEqual(filter_by_substring(strings, substring), expected_output)

    def test_filter_by_substring_empty_list(self):
        strings = []
        substring = 'ab'
        expected_output = []
        self.assertEqual(filter_by_substring(strings, substring), expected_output)

    def test_filter_by_substring_no_match(self):
        strings = ['xyz', 'def', 'ab']
        substring = 'ab'
        expected_output = []
        self.assertEqual(filter_by_substring(strings, substring), expected_output)

    def test_filter_by_substring_single_element(self):
        strings = ['abc']
        substring = 'ab'
        expected_output = ['abc']
        self.assertEqual(filter_by_substring(strings, substring), expected_output)

    def test_filter_by_substring_case_insensitive(self):
        strings = ['Abc', 'def', 'aB']
        substring = 'ab'
        expected_output = ['Abc', 'aB']
        self.assertEqual(filter_by_substring(strings, substring), expected_output)

if __name__ == '__main__':
    unittest.main()