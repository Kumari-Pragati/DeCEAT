Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `filter_by_substring` function:


import unittest
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(filter_by_substring([], 'abc'), [])

    def test_single_string(self):
        self.assertListEqual(filter_by_substring(['abc'], 'abc'), ['abc'])
        self.assertListEqual(filter_by_substring(['abc'], 'def'), [])

    def test_multiple_strings(self):
        self.assertListEqual(filter_by_substring(['abc', 'def', 'ab'], 'ab'), ['abc', 'ab'])
        self.assertListEqual(filter_by_substring(['abc', 'def', 'ab'], 'def'), [])
        self.assertListEqual(filter_by_substring(['abc', 'xyz', 'ab'], 'xyz'), [''])

    def test_case_insensitive(self):
        self.assertListEqual(filter_by_substring(['AbC', 'dEf', 'aB'], 'ab'), ['AbC', 'aB'])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, including an empty list, a single string, multiple strings, case-insensitive matching, and a test case where no strings match the substring. The test cases use the `assertListEqual` method to check that the expected output matches the actual output of the `filter_by_substring` function.