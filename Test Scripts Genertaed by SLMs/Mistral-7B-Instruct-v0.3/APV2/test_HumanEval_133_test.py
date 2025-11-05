You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_133_code import sum_squares
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sum_squares(lst):
    """You are given a list of numbers.
    You need to return the sum of squared numbers in the given list,
    round each element in the list to the upper int(Ceiling) first.
    Examples:
    For lst = [1,2,3] the output should be 14
    For lst = [1,4,9] the output should be 98
    For lst = [1,3,5,7] the output should be 84
    For lst = [1.4,4.2,0] the output should be 29
    For lst = [-2.4,1,1] the output should be 6
    """
    import math
    squared = 0
    for i in lst:
        squared += math.ceil(i) ** 2
    return squared

 Here is the complete unittest test suite for the `sum_squares` function:


import unittest
from HumanEval_133_code import sum_squares

class TestSumSquares(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sum_squares([]), 0)

    def test_single_element(self):
        self.assertEqual(sum_squares([0]), 0)
        self.assertEqual(sum_squares([1]), 1)
        self.assertEqual(sum_squares([-1]), 1)

    def test_positive_numbers(self):
        self.assertEqual(sum_squares([1, 2, 3]), 14)
        self.assertEqual(sum_squares([1, 4, 9]), 98)
        self.assertEqual(sum_squares([1, 3, 5, 7]), 84)

    def test_negative_numbers(self):
        self.assertEqual(sum_squares([-1, -2, -3]), 14)
        self.assertEqual(sum_squares([-2.4, -1, 1]), 6)

    def test_floating_point_numbers(self):
        self.assertEqual(sum_squares([1.4, 4.2, 0]), 29)
        self.assertEqual(sum_squares([-2.4, 1, 1]), 6)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for empty lists, single elements, positive numbers, negative numbers, and floating-point numbers. It covers various edge cases and ensures that the `sum_squares` function behaves as expected.