Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `sort_array` function:


import unittest
from HumanEval_116_code import sort_array

class TestSortArray(unittest.TestCase):

    def test_sort_array(self):
        self.assertEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(sort_array([-2, -3, -4, -5, -6]), [-6, -5, -4, -3, -2])
        self.assertEqual(sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 3, 4])
        self.assertEqual(sort_array([10, 20, 11, 21, 12, 22]), [10, 11, 12, 20, 21, 22])
        self.assertEqual(sort_array([100, 101, 110, 111, 1000, 1001]), [100, 1000, 101, 110, 111])
        self.assertEqual(sort_array([0, 0, 1, 1, 2, 2]), [0, 0, 1, 1, 2, 2])
        self.assertEqual(sort_array([10, 11, 12, 13, 14, 15]), [10, 11, 12, 13, 14, 15])
        self.assertEqual(sort_array([2147483647, 0]), [0, 2147483647])
        self.assertEqual(sort_array([]), [])

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases for the `sort_array` function and checks if the function behaves as expected. The test cases cover different scenarios such as positive and negative numbers, zeroes, and edge cases.