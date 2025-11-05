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

 Here is a comprehensive unittest test suite for the given Python function `monotonic`.


import unittest
from HumanEval_57_code import monotonic

class TestMonotonic(unittest.TestCase):
    def test_monotonic_increasing(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))
        self.assertTrue(monotonic([0, 1, 2, 3, 4, 5]))
        self.assertTrue(monotonic([-10, -9, -8, -7, -6]))

    def test_monotonic_decreasing(self):
        self.assertTrue(monotonic([4, 3, 2, 1]))
        self.assertTrue(monotonic([5, 4, 3, 2, 1]))
        self.assertTrue(monotonic([10, 11, 12, 13, 14]))

    def test_non_monotonic(self):
        self.assertFalse(monotonic([1, 20, 4, 10]))
        self.assertFalse(monotonic([4, 1, 0, -10, 20]))
        self.assertFalse(monotonic([20, 1, 2, 3, 4]))

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_monotonic_increasing` checks that the function correctly identifies monotonically increasing lists.
2. `test_monotonic_decreasing` checks that the function correctly identifies monotonically decreasing lists.
3. `test_non_monotonic` checks that the function correctly identifies non-monotonic lists.

Each test case includes multiple examples to ensure the function behaves correctly for a variety of inputs.