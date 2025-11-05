You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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
        self.assertEqual(filter_by_substring(['abc', 'ab', 'bca'], 'abc'), ['abc'])

    def test_substring_at_end(self):
        self.assertEqual(filter_by_substring(['abc', 'ab', 'bca'], 'bca'), ['bca'])

    def test_substring_in_middle(self):
        self.assertEqual(filter_by_substring(['abc', 'ab', 'bca'], 'bc'), ['abc', 'ab', 'bca'])

    def test_empty_substring(self):
        self.assertEqual(filter_by_substring(['abc', 'ab', 'bca'], ''), ['abc', 'ab', 'bca'])

if __name__ == '__main__':
    unittest.main()


This test suite covers a variety of scenarios, including an empty list, no matches, single match, multiple matches, substrings at the start, end, and middle of strings, and an empty substring.