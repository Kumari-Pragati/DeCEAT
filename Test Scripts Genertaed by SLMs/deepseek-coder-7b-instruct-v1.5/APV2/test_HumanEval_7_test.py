You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(filter_by_substring([], 'ab'), [])

    def test_no_match(self):
        self.assertEqual(filter_by_substring(['abc', 'def', 'xyz'], 'ab'), [])

    def test_single_match(self):
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'ab'), ['abc', 'ab'])

    def test_multiple_matches(self):
        self.assertEqual(filter_by_substring(['abc', 'ab', 'bca', 'cab'], 'ab'), ['abc', 'ab', 'bca', 'cab'])

    def test_substring_at_start(self):
        self.assertEqual(filter_by_substring(['abc', 'ab'], 'ab'), ['abc', 'ab'])

    def test_substring_at_end(self):
        self.assertEqual(filter_by_substring(['ab', 'abc'], 'ab'), ['ab', 'abc'])

    def test_substring_in_middle(self):
        self.assertEqual(filter_by_substring(['abc', 'abd', 'abe'], 'ab'), ['abc', 'abd', 'abe'])

    def test_case_sensitivity(self):
        self.assertEqual(filter_by_substring(['Abc', 'ab'], 'ab'), [])

if __name__ == '__main__':
    unittest.main()


This suite includes tests for different scenarios: empty list, no match, single match, multiple matches, substring at the start, substring at the end, substring in the middle, and case sensitivity.