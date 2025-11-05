user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return [x for x in strings if x.startswith(prefix)]assistant

Here is the unittest test script for the `filter_by_prefix` function:

import unittest
from HumanEval_29_code import filter_by_prefix

class TestFilterByPrefix(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(filter_by_prefix([], 'a'), [])

    def test_no_matches(self):
        self.assertEqual(filter_by_prefix(['xyz', 'bcd', 'cde'], 'a'), [])

    def test_single_match(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde'], 'a'), ['abc'])

    def test_multiple_matches(self):
        self.assertEqual(filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a'), ['abc', 'array'])

    def test_prefix_with_spaces(self):
        self.assertEqual(filter_by_prefix(['abc def', 'bcd efg', 'cde fgh'], 'a '), ['abc def', 'array'])

    def test_prefix_with_special_chars(self):
        self.assertEqual(filter_by_prefix(['abc!@#', 'bcd$%^', 'cde*()'], 'a'), ['abc!@#'])

    def test_prefix_with_non_ascii_chars(self):
        self.assertEqual(filter_by_prefix(['abcé', 'bcdü', 'cdeö'], 'a'), ['abcé'])

if __name__ == '__main__':
    unittest.main()

This test script covers various scenarios, including:

1. An empty input list
2. No matches found
3. A single match
4. Multiple matches
5. A prefix with spaces
6. A prefix with special characters
7. A prefix with non-ASCII characters

Each test method uses the `assertEqual` method to verify that the output of the `filter_by_prefix` function matches the expected result.