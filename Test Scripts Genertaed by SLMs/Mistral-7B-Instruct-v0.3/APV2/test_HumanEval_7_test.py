You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the `filter_by_substring` function:


import unittest
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(filter_by_substring([], 'abc'), [])

    def test_single_element(self):
        self.assertListEqual(filter_by_substring(['abc'], 'abc'), ['abc'])

    def test_single_substring_not_found(self):
        self.assertListEqual(filter_by_substring(['abc', 'def'], 'ghi'), [])

    def test_multiple_elements_with_substring(self):
        self.assertListEqual(filter_by_substring(['abc', 'ab', 'def', 'xyzabcd'], 'ab'), ['ab', 'xyzabcd'])

    def test_multiple_elements_without_substring(self):
        self.assertListEqual(filter_by_substring(['abc', 'def', 'xyzabcd'], 'ghi'), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover different scenarios, such as an empty list, single elements, multiple elements containing the substring, and multiple elements without the substring. The `assertListEqual` function is used to verify that the expected output matches the actual output returned by the `filter_by_substring` function.