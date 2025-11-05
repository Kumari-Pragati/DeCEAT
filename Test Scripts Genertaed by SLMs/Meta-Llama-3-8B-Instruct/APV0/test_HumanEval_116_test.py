user

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
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_116_code import sort_array

class TestSortArray(unittest.TestCase):

    def test_sort_array(self):
        self.assertEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(sort_array([-2, -3, -4, -5, -6]), [-6, -5, -4, -3, -2])
        self.assertEqual(sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 3, 4])
        self.assertEqual(sort_array([1, 1, 0, 1, 0]), [0, 0, 0, 1, 1])
        self.assertEqual(sort_array([5, 2, 1, 3, 4]), [1, 2, 3, 4, 5])
        self.assertEqual(sort_array([1, 1, 1, 1, 1]), [1, 1, 1, 1, 1])
        self.assertEqual(sort_array([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(sort_array([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])
        self.assertEqual(sort_array([1, 1, 1, 1, 1, 1]), [1, 1, 1, 1, 1, 1])

    def test_sort_array_empty(self):
        self.assertEqual(sort_array([]), [])

    def test_sort_array_single_element(self):
        self.assertEqual(sort_array([1]), [1])

    def test_sort_array_single_element_zero(self):
        self.assertEqual(sort_array([0]), [0])

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to ensure the function is working correctly. The test cases cover a variety of scenarios, including arrays with different lengths, arrays with and without zeros, and arrays with and without duplicates.