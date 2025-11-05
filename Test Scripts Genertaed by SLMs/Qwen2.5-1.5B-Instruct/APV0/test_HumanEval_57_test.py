system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_57_code import monotonic
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def monotonic(l: list):
    """Return True if list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if l == sorted(l) or l == sorted(l, reverse=True):
        return True
    return False


assistant

import unittest

# Importing the function to be tested
from HumanEval_57_code import monotonic

class TestMonotonic(unittest.TestCase):

    def test_monotonic(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))
        self.assertFalse(monotonic([1, 20, 4, 10]))
        self.assertTrue(monotonic([4, 1, 0, -10]))

if __name__ == '__main__':
    unittest.main()


This script imports the `monotonic` function from the `HumanEval_57_code` module and defines a test class `TestMonotonic` within the `unittest` framework. The `test_monotonic` method contains assertions that check whether the `monotonic` function returns the expected results for different input lists. If all tests pass, it will run the entire test suite when executed directly.