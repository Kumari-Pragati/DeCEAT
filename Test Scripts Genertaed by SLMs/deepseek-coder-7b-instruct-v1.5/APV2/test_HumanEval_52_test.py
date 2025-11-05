You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_52_code import below_threshold
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for e in l:
        if e >= t:
            return False
    return True


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_52_code import below_threshold

class TestBelowThreshold(unittest.TestCase):

    def test_all_below(self):
        self.assertTrue(below_threshold([1, 2, 3, 4], 5))

    def test_one_above(self):
        self.assertFalse(below_threshold([1, 2, 3, 5], 5))

    def test_all_above(self):
        self.assertFalse(below_threshold([6, 7, 8, 9], 5))

    def test_empty_list(self):
        self.assertTrue(below_threshold([], 5))

    def test_negative_numbers(self):
        self.assertFalse(below_threshold([-1, -2, -3, -4], -1))

    def test_mixed_numbers(self):
        self.assertFalse(below_threshold([1, -2, 3, -4], 1))

if __name__ == '__main__':
    unittest.main()


This suite includes tests for different scenarios:

1. When all numbers in the list are below the threshold.
2. When one number in the list is above the threshold.
3. When all numbers in the list are above the threshold.
4. When the list is empty.
5. When the list contains negative numbers.
6. When the list contains both positive and negative numbers.

Each test case checks the function's behavior under a specific scenario.