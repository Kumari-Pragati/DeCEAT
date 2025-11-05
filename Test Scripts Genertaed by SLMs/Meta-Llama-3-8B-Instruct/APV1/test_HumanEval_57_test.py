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
    return Falseassistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_57_code import monotonic

class TestMonotonic(unittest.TestCase):

    def test_monotonic_increasing(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))
        self.assertTrue(monotonic([4, 5, 6, 7]))
        self.assertTrue(monotonic([1, 2, 3, 4]))
        self.assertTrue(monotonic([0, 1, 2, 3]))

    def test_monotonic_decreasing(self):
        self.assertTrue(monotonic([4, 3, 2, 1]))
        self.assertTrue(monotonic([20, 10, 5, 1]))
        self.assertTrue(monotonic([10, 5, 2, 0]))
        self.assertTrue(monotonic([-10, -5, -2, -1]))

    def test_monotonic_mixed(self):
        self.assertFalse(monotonic([1, 20, 4, 10]))
        self.assertFalse(monotonic([4, 1, 2, 3]))
        self.assertFalse(monotonic([1, 2, 3, 4, 5]))
        self.assertFalse(monotonic([0, 1, 2, 3, 4]))

    def test_monotonic_empty(self):
        self.assertFalse(monotonic([]))

    def test_monotonic_single_element(self):
        self.assertTrue(monotonic([1]))
        self.assertTrue(monotonic([-1]))
        self.assertTrue(monotonic([0]))

    def test_monotonic_all_equal(self):
        self.assertTrue(monotonic([1, 1, 1, 1]))
        self.assertTrue(monotonic([0, 0, 0, 0]))
        self.assertTrue(monotonic([-1, -1, -1, -1]))

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the following cases:
- Monotonic increasing lists
- Monotonic decreasing lists
- Mixed lists (not monotonic)
- Empty lists
- Single-element lists
- Lists with all equal elements

Each test case checks the output of the `monotonic` function against the expected result.