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

 Here is a unittest test script for the `monotonic` function:


import unittest
from HumanEval_57_code import monotonic

class TestMonotonic(unittest.TestCase):
    def test_monotonic_increasing(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))
        self.assertTrue(monotonic([0, 1, 2, 3, 4, 5]))
        self.assertTrue(monotonic([-1, -2, -3, -4, -5]))

    def test_monotonic_decreasing(self):
        self.assertTrue(monotonic([4, 3, 2, 1]))
        self.assertTrue(monotonic([5, 4, 3, 2, 1]))
        self.assertTrue(monotonic([5, 4, -3, -4, -5]))

    def test_non_monotonic(self):
        self.assertFalse(monotonic([1, 20, 4, 10]))
        self.assertFalse(monotonic([0, 2, 1]))
        self.assertFalse(monotonic([4, 1, 3, 0]))

if __name__ == '__main__':
    unittest.main()


This test script includes three test cases:

1. `test_monotonic_increasing` checks that the function correctly identifies monotonically increasing lists.
2. `test_monotonic_decreasing` checks that the function correctly identifies monotonically decreasing lists.
3. `test_non_monotonic` checks that the function correctly identifies non-monotonic lists.

You can run this test script directly by saving it as a .py file and running it using the command `python filename.py`. The output should show that all test cases pass.