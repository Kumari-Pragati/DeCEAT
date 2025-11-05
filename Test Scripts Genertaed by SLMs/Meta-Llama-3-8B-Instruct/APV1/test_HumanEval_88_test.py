user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_88_code import sort_array
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting.
    You will sort the given array in ascending order if the sum(first index value, last index value) is odd,
    or sort it in descending order if the sum(first index value, last index value) is even.

    Note:
    * Don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """

    return [] if len(array) == 0 else sorted(array, reverse=(array[0] + array[-1]) % 2 == 0)assistant

Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_88_code import sort_array

class TestSortArray(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(sort_array([]), [])

    def test_single_element_array(self):
        self.assertEqual(sort_array([5]), [5])

    def test_small_array(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])

    def test_large_array(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])

    def test_array_with_duplicates(self):
        self.assertEqual(sort_array([2, 2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 2, 1, 0])

    def test_array_with_negative_numbers(self):
        self.assertEqual(sort_array([-2, -4, -3, 0, 1, 5, 6]), [6, 5, 1, 0, -3, -4, -2])

    def test_array_with_mixed_positive_and_negative_numbers(self):
        self.assertEqual(sort_array([-2, 4, -3, 0, 1, 5, 6]), [6, 5, 1, 0, -3, -2, 4])

    def test_array_with_all_negative_numbers(self):
        self.assertEqual(sort_array([-2, -4, -3, -1, -5, -6]), [-6, -5, -4, -3, -2, -1])

    def test_array_with_all_positive_numbers(self):
        self.assertEqual(sort_array([2, 4, 3, 1, 5, 6]), [6, 5, 4, 3, 2, 1])

    def test_array_with_all_zeroes(self):
        self.assertEqual(sort_array([0, 0, 0, 0, 0, 0]), [0, 0, 0, 0, 0, 0])

    def test_array_with_mixed_zeroes_and_non_zero_numbers(self):
        self.assertEqual(sort_array([0, 2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0, 0])

if __name__ == '__main__':
    unittest.main()


This test suite covers a variety of test cases, including:

* Empty array
* Single-element array
* Small array
* Large array
* Array with duplicates
* Array with negative numbers
* Array with mixed positive and negative numbers
* Array with all negative numbers
* Array with all positive numbers
* Array with all zeroes
* Array with mixed zeroes and non-zero numbers

Each test case checks that the output of the `sort_array` function is as expected.