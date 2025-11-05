You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_116_code import sort_array

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))

 Here is a comprehensive unittest test suite for the given Python function `sort_array`. The test cases cover various scenarios, including empty lists, negative numbers, and a mix of numbers with different numbers of ones in their binary representation.


import unittest
from HumanEval_116_code import sort_array

class TestSortArray(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_array([]), [])

    def test_single_element(self):
        self.assertEqual(sort_array([0]), [0])
        self.assertEqual(sort_array([1]), [1])
        self.assertEqual(sort_array([2]), [2])

    def test_positive_numbers(self):
        self.assertEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(sort_array([10, 20, 15, 25, 12]), [10, 12, 15, 20, 25])
        self.assertEqual(sort_array([100, 200, 150, 250, 120]), [100, 120, 150, 200, 250])

    def test_negative_numbers(self):
        self.assertEqual(sort_array([-2, -3, -4, -5, -6]), [-6, -5, -4, -3, -2])
        self.assertEqual(sort_array([-10, -20, -15, -25, -12]), [-10, -12, -15, -20, -25])
        self.assertEqual(sort_array([-100, -200, -150, -250, -120]), [-100, -120, -150, -200, -250])

    def test_mixed_numbers(self):
        self.assertEqual(sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 3, 4])
        self.assertEqual(sort_array([10, 0, 20, 30, 40]), [0, 10, 20, 30, 40])
        self.assertEqual(sort_array([100, 0, 200, 300, 400]), [0, 100, 200, 300, 400])

if __name__ == '__main__':
    unittest.main()


This test suite includes test cases for empty lists, single elements, positive numbers, negative numbers, and a mix of positive and negative numbers. The test cases cover various scenarios where the number of ones in the binary representation of the numbers can be different.