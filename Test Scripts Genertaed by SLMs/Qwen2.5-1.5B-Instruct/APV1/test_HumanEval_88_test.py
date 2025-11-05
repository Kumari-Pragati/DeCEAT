system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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

    return [] if len(array) == 0 else sorted(array, reverse=(array[0] + array[-1]) % 2 == 0)


assistant

import unittest

# Function to be tested
from HumanEval_88_code import sort_array

class TestSortArray(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(sort_array([]), [])

    def test_single_element(self):
        self.assertEqual(sort_array([5]), [5])

    def test_odd_sum_first_last(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5]), [0, 1, 2, 3, 4, 5])

    def test_even_sum_first_last(self):
        self.assertEqual(sort_array([2, 4, 3, 0, 1, 5, 6]), [6, 5, 4, 3, 2, 1, 0])

    def test_mixed_elements(self):
        self.assertEqual(sort_array([7, 9, 1, 3, 5, 2]), [1, 2, 3, 5, 7, 9])

    def test_sorted_in_descending_order(self):
        self.assertEqual(sort_array([9, 7, 5, 3, 1]), [1, 3, 5, 7, 9])

    def test_sorted_in_ascending_order(self):
        self.assertEqual(sort_array([1, 3, 5, 7, 9]), [1, 3, 5, 7, 9])

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestSortArray` class that inherits from `unittest.TestCase`. It contains several test methods to verify the correctness of the `sort_array` function. The tests cover various scenarios including empty arrays, single elements, arrays with both odd and even sums, mixed elements, sorted in descending order, and sorted in ascending order. If you run this script directly (i.e., not as part of another module), it will execute all the defined test cases using `unittest.main()`.