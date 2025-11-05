system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Provided function
from HumanEval_7_code import filter_by_substring

class TestFilterBySubstring(unittest.TestCase):
    
    def test_filter_by_substring(self):
        # Test case 1: Contains substring
        self.assertEqual(filter_by_substring(['abc', 'def', 'ab'], 'ab'), ['abc', 'ab'])
        
        # Test case 2: Does not contain substring
        self.assertEqual(filter_by_substring(['hello', 'world', 'hi'], 'bye'), [])
        
        # Test case 3: Single element list
        self.assertEqual(filter_by_substring(['single'], ''), ['single'])
        
        # Test case 4: Empty input
        self.assertEqual(filter_by_substring([], 'any'), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases to verify the functionality of the `filter_by_substring` function. It checks various scenarios including when the substring is present or absent in each string, as well as handling single-element lists and empty inputs.