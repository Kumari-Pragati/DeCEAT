system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

Here is the complete unittest test suite for the given Python function:


import unittest
from HumanEval_57_code import monotonic

class TestMonotonic(unittest.TestCase):

    def test_monotonic_increasing(self):
        self.assertTrue(monotonic([1, 2, 4, 20]))
        self.assertTrue(monotonic([4, 5, 7, 10]))
        self.assertTrue(monotonic([10, 12, 15, 20]))

    def test_monotonic_decreasing(self):
        self.assertTrue(monotonic([20, 15, 12, 10]))
        self.assertTrue(monotonic([10, 7, 5, 4]))
        self.assertTrue(monotonic([4, 2, 1]))

    def test_monotonic_mixed(self):
        self.assertFalse(monotonic([1, 20, 4, 10]))
        self.assertFalse(monotonic([4, 10, 20, 1]))
        self.assertFalse(monotonic([10, 5, 2, 1]))

    def test_monotonic_empty(self):
        self.assertTrue(monotonic([]))

    def test_monotonic_single_element(self):
        self.assertTrue(monotonic([1]))

    def test_monotonic_all_equal(self):
        self.assertTrue(monotonic([1, 1, 1, 1]))

    def test_monotonic_all_equal_reverse(self):
        self.assertTrue(monotonic([1, 1, 1, 1], reverse=True))

if __name__ == '__main__':
    unittest.main()