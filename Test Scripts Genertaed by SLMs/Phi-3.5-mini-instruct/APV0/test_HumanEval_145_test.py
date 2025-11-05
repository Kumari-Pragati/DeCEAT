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

 import unittest
from HumanEval_145_code import order_by_points

class TestOrderByPoints(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(order_by_points([]), [])

    def test_single_element_list(self):
        self.assertEqual(order_by_points([1]), [1])
        self.assertEqual(order_by_points([-1]), [-1])

    def test_multiple_elements_list(self):
        self.assertEqual(order_by_points([1, 11, -1, -11, -12]), [-1, -11, 1, -12, 11])
        self.assertEqual(order_by_points([10, 2, -3, 4, -5]), [-3, 2, 4, 10, -5])
        self.assertEqual(order_by_points([100, 20, -30, 40, -50]), [-30, 20, 40, 100, -50])
        self.assertEqual(order_by_points([1000, -200, 300, -400, 500]), [-400, 300, 1000, -200, -500])

    def test_negative_numbers(self):
        self.assertEqual(order_by_points([-1, -11, -12, -100]), [-1, -11, -12, -100])

    def test_same_digit_sum_order(self):
        self.assertEqual(order_by_points([10, 20, 30, 40]), [10, 20, 30, 40])
        self.assertEqual(order_by_points([100, 200, 300, 400]), [100, 200, 300, 400])

    def test_same_digit_sum_with_negatives(self):
        self.assertEqual(order_by_points([-10, -20, -30, -40]), [-40, -30, -20, -10])

if __name__ == '__main__':
    unittest.main()