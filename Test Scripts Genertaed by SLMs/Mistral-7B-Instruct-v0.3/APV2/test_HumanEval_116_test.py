You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the `sort_array` function:


import unittest
from HumanEval_116_code import sort_array

class TestSortArray(unittest.TestCase):

    def test_sort_array_simple(self):
        self.assertEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(sort_array([-2, -3, -4, -5, -6]), [-6, -5, -4, -3, -2])
        self.assertEqual(sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 3, 4])

    def test_sort_array_mixed(self):
        self.assertEqual(sort_array([10, 2, 1, 20, 100, 1000, 1001]), [1, 2, 10, 100, 1000, 1001, 20])
        self.assertEqual(sort_array([0, 1, 2, 3, 4, 5, 6]), [0, 1, 2, 3, 4, 5, 6])
        self.assertEqual(sort_array([10, 11, 12, 13, 14]), [10, 11, 12, 13, 14])

    def test_sort_array_edge_cases(self):
        self.assertEqual(sort_array([0]), [0])
        self.assertEqual(sort_array([2**32]), [2**32])
        self.assertEqual(sort_array([2**32 - 1]), [2**32 - 1])

if __name__ == '__main__':
    unittest.main()


This test suite includes multiple test cases for different scenarios, including simple cases, mixed cases, and edge cases. The test cases are designed to cover a wide range of inputs and ensure that the `sort_array` function behaves as expected.