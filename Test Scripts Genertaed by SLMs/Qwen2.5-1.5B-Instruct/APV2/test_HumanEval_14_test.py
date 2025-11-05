system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_14_code import all_prefixes
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    result: List[str] = []
    for i in range(len(string)):
        result.append(string[: i + 1])
    return result


assistant

import unittest

# Provided function
from HumanEval_14_code import all_prefixes

class TestAllPrefixes(unittest.TestCase):
    
    def test_all_prefixes(self):
        # Test case 1: Empty string
        self.assertEqual(all_prefixes(""), [])
        
        # Test case 2: Single character string
        self.assertEqual(all_prefixes("a"), ["a"])
        
        # Test case 3: String with multiple characters
        self.assertEqual(all_prefixes("abc"), ["a", "ab", "abc"])
        
        # Test case 4: String with repeated characters
        self.assertEqual(all_prefixes("aaa"), ["a", "aa", "aaa"])

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases that cover various scenarios as described in the docstring of `all_prefixes`. It uses the `assertEqual` method to check if the returned list matches the expected output for each test case.