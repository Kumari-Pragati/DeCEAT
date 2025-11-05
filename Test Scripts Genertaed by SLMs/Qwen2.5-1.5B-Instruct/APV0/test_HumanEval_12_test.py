system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_12_code import longest
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None

    maxlen = max(len(x) for x in strings)
    for s in strings:
        if len(s) == maxlen:
            return s


assistant

import unittest

# Function to test
from HumanEval_12_code import longest

class TestLongest(unittest.TestCase):
    
    def test_empty_list(self):
        self.assertIsNone(longest([]))

    def test_single_element(self):
        self.assertEqual(longest(["single"]), "single")

    def test_multiple_elements(self):
        self.assertEqual(longest(["one", "two", "three"]), "three")
        self.assertEqual(longest(["aa", "bb", "cc"]), "cc")

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a class `TestLongest` that inherits from `unittest.TestCase`. It contains three test methods:

- `test_empty_list`: Tests the function with an empty list, expecting `None`.
- `test_single_element`: Tests the function with a single-element list, expecting the element itself.
- `test_multiple_elements`: Tests the function with lists containing multiple elements, comparing the expected result against the actual result.

Finally, it calls `unittest.main()` to run all tests when the script is executed directly.