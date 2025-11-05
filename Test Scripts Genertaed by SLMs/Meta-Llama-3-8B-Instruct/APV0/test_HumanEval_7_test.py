user

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
    return [x for x in strings if substring in x]assistant

Here is the unittest test script for the `filter_by_substring` function:

import unittest
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'abc'), [])

    def test_no_matches(self):
        self.assertEqual(filter_by_substring(['def', 'ghi'], 'jkl'), [])

    def test_single_match(self):
        self.assertEqual(filter_by_substring(['abc', 'def', 'ghi'], 'abc'), ['abc'])

    def test_multiple_matches(self):
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab', 'ghi'], 'ab'), ['abc', 'ab'])

    def test_substring_in_all_strings(self):
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'ab'), ['abc', 'ab'])

    def test_substring_not_in_all_strings(self):
        self.assertEqual(filter_by_substring(['abc', 'def', 'ghi'], 'jkl'), [])

    def test_substring_in_first_string(self):
        self.assertEqual(filter_by_substring(['abc', 'def', 'ghi'], 'abc'), ['abc'])

    def test_substring_in_last_string(self):
        self.assertEqual(filter_by_substring(['ghi', 'def', 'abc'], 'abc'), ['abc'])

    def test_substring_in_middle_string(self):
        self.assertEqual(filter_by_substring(['def', 'abc', 'ghi'], 'abc'), ['abc'])

if __name__ == '__main__':
    unittest.main()

This test script covers a variety of scenarios to ensure the `filter_by_substring` function is working correctly. It tests:

1. An empty list of strings
2. A list with no matches for the substring
3. A list with a single match for the substring
4. A list with multiple matches for the substring
5. A list where the substring is present in all strings
6. A list where the substring is not present in any strings
7. A list where the substring is present in the first string
8. A list where the substring is present in the last string
9. A list where the substring is present in the middle string

Each test case checks the output of the `filter_by_substring` function against the expected result using the `assertEqual` method.