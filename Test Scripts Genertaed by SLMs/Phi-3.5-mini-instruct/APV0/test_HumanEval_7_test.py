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

 import unittest
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):

    def test_filter_by_substring(self):
        # Test case where all strings contain the substring
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'ab'), ['abc', 'ab'])

        # Test case where some strings contain the substring
        self.assertEqual(filter_by_substring(['abc', 'def', 'ghi'], 'ab'), ['abc'])

        # Test case where no strings contain the substring
        self.assertEqual(filter_by_substring(['xyz', 'lmn', 'opq'], 'ab'), [])

        # Test case with an empty list
        self.assertEqual(filter_by_substring([], 'ab'), [])

        # Test case with an empty substring
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], ''), ['abc', 'ab'])

        # Test case with a single string
        self.assertEqual(filter_by_substring(['abc'], 'ab'), ['abc'])

        # Test case with a single substring
        self.assertEqual(filter_by_substring(['ab'], 'ab'), ['ab'])

        # Test case with case-insensitive matching
        self.assertEqual(filter_by_substring(['Abc', 'DEF', 'aB'], 'ab'), ['Abc', 'aB'])

        # Test case with mixed case strings
        self.assertEqual(filter_by_substring(['aBc', 'DeF', 'gHi'], 'ab'), ['aBc'])

        # Test case with non-string elements
        self.assertEqual(filter_by_substring(['123', 'abc', 456], 'ab'), ['abc'])

        # Test case with None values
        self.assertEqual(filter_by_substring(['abc', None, 'def'], 'ab'), ['abc'])

        # Test case with empty strings
        self.assertEqual(filter_by_substring(['', 'abc', 'def'], 'ab'), ['abc'])

if __name__ == '__main__':
    unittest.main()