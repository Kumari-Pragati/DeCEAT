system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

# Importing the function from the given code snippet
from HumanEval_14_code import all_prefixes

class TestAllPrefixes(unittest.TestCase):
    def test_all_prefixes(self):
        # Test case 1: Empty string
        self.assertEqual(all_prefixes(""), [])

        # Test case 2: Single character string
        self.assertEqual(all_prefixes("a"), ["a"])

        # Test case 3: String with multiple characters
        self.assertEqual(all_prefixes("abc"), ["", "a", "ab", "abc"])

        # Test case 4: String with repeated characters
        self.assertEqual(all_prefixes("aaa"), ["", "a", "aa", "aaa"])

        # Test case 5: String with special characters
        self.assertEqual(all_prefixes("hello!"), ["!", "h", "he", "hel", "hell", "hello"])

if __name__ == '__main__':
    unittest.main()


This script imports the `all_prefixes` function from the provided code snippet and defines a test class `TestAllPrefixes` that contains several test cases using the `assertEqual` method to verify the correctness of the function. The `unittest.main()` call at the end makes the tests executable when run as a standalone script.