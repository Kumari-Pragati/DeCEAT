Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `order_by_points` function:


import unittest
from HumanEval_145_code import order_by_points

class TestOrderByPoints(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(order_by_points([]), [])

    def test_single_element(self):
        self.assertEqual(order_by_points([1]), [1])

    def test_positive_numbers(self):
        self.assertEqual(order_by_points([1, 11, 101, 111]), [1, 11, 101, 111])

    def test_negative_numbers(self):
        self.assertEqual(order_by_points([-1, -11, -101, -111]), [-1, -11, -101, -111])

    def test_mixed_numbers(self):
        self.assertEqual(order_by_points([1, -1, 11, -11, 101, -101, 111, -111]), [-1, -11, 1, -101, -111, 11, 101, 111])

    def test_complex_numbers(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12, -111, 111, -1011]), [-1, -11, -111, -1011, 1, -12, 11, 111])

if __name__ == '__main__':
    unittest.main()


This test script includes multiple test cases to cover various scenarios, such as an empty list, single elements, positive numbers, negative numbers, mixed numbers, and complex numbers. The test cases are designed to ensure that the `order_by_points` function works correctly for different input cases.