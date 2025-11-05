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
    return Falseassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_57_code import monotonic

class TestMonotonic(unittest.TestCase):

    def test_monotonic_increasing(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))
        self.assertTrue(monotonic([4, 5, 6, 7]))
        self.assertTrue(monotonic([10, 11, 12, 13]))

    def test_monotonic_decreasing(self):
        self.assertTrue(monotonic([20, 10, 4, 1]))
        self.assertTrue(monotonic([7, 6, 5, 4]))
        self.assertTrue(monotonic([-10, -11, -12, -13]))

    def test_monotonic_mixed(self):
        self.assertFalse(monotonic([1, 20, 4, 10]))
        self.assertFalse(monotonic([4, 1, 2, 3]))
        self.assertFalse(monotonic([10, 9, 8, 7]))

    def test_monotonic_empty(self):
        self.assertTrue(monotonic([]))

    def test_monotonic_single_element(self):
        self.assertTrue(monotonic([1]))
        self.assertTrue(monotonic([-1]))

    def test_monotonic_all_equal(self):
        self.assertTrue(monotonic([1, 1, 1, 1]))

if __name__ == '__main__':
    unittest.main()


This script includes test cases for the following scenarios:
- Monotonic increasing
- Monotonic decreasing
- Mixed (both increasing and decreasing)
- Empty list
- Single-element list
- All equal elements

Each test case checks if the function returns the expected result.