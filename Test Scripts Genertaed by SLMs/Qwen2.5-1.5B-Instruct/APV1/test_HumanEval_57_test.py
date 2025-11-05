system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

# Function to be tested
from HumanEval_57_code import monotonic

class TestMonotonic(unittest.TestCase):

    def test_monotonic(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))
        self.assertFalse(monotonic([1, 20, 4, 10]))
        self.assertTrue(monotonic([4, 1, 0, -10]))

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestMonotonic` class that inherits from `unittest.TestCase`. It contains a single method `test_monotonic`, which tests the `monotonic` function using assertions. The `assertTrue`, `assertFalse`, and `assertTrue` methods are used to check whether the output of the `monotonic` function matches the expected results. Finally, the `unittest.main()` call at the end runs all the tests defined in the `TestMonotonic` class.