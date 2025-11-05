system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_145_code import order_by_points
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """
    def digits_sum(n):
        neg = 1
        if n < 0:
            n, neg = -1 * n, -1
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)

    return sorted(nums, key=digits_sum)


assistant

import unittest

# Function to be tested
from HumanEval_145_code import order_by_points


class TestOrderByPoints(unittest.TestCase):

    def test_order_by_points(self):
        # Test cases
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
        self.assertEqual(order_by_points([]), [])
        self.assertEqual(order_by_points([-1, 11, -11, 1, 12]), [-1, -11, 1, 11, 12])

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases to verify the correctness of the `order_by_points` function. The first two test cases check that the function returns the expected results for positive numbers, negative numbers, and empty lists. The third case tests the function with a mix of positive and negative numbers to ensure it correctly orders them based on the sum of their digits.