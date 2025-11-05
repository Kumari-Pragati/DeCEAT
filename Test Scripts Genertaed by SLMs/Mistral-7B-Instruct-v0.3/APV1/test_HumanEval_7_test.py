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

 Here is a comprehensive unittest test suite for the `filter_by_substring` function:


import unittest
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(filter_by_substring([], 'abc'), [])

    def test_single_element(self):
        self.assertListEqual(filter_by_substring(['abc'], 'abc'), ['abc'])
        self.assertListEqual(filter_by_substring(['abc'], 'def'), [])

    def test_multiple_elements(self):
        self.assertListEqual(filter_by_substring(['abc', 'def', 'ab'], 'ab'), ['abc', 'ab'])
        self.assertListEqual(filter_by_substring(['abc', 'def', 'ab'], 'def'), [])
        self.assertListEqual(filter_by_substring(['abc', 'xyz', '123'], 'abc'), ['abc'])

    def test_case_insensitive(self):
        self.assertListEqual(filter_by_substring(['AbC', 'dEf', 'aB'], 'ab'), ['AbC', 'aB'])

    def test_substring_not_found(self):
        self.assertListEqual(filter_by_substring(['abc', 'def', 'ab'], 'xyz'), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as an empty list, single elements, multiple elements, case-insensitivity, and when the substring is not found in any of the strings.