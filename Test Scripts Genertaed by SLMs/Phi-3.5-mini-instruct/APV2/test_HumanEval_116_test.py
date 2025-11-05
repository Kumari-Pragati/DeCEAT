You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
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

 
import unittest
from HumanEval_116_code import sort_array

class TestSortArray(unittest.TestCase):

    def test_sort_array_with_positive_integers(self):
        self.assertEqual(sort_array([1, 5, 2, 3, 4]), [1, 2, 3, 4, 5])

    def test_sort_array_with_negative_integers(self):
        self.assertEqual(sort_array([-2, -3, -4, -5, -6]), [-6, -5, -4, -3, -2])

    def test_sort_array_with_mixed_integers(self):
        self.assertEqual(sort_array([1, 0, 2, 3, 4]), [0, 1, 2, 3, 4])

    def test_sort_array_with_empty_list(self):
        self.assertEqual(sort_array([]), [])

    def test_sort_array_with_single_element(self):
        self.assertEqual(sort_array([5]), [5])

    def test_sort_array_with_duplicate_elements(self):
        self.assertEqual(sort_array([1, 1, 2, 2, 3, 3]), [1, 1, 2, 2, 3, 3])

    def test_sort_array_with_zero(self):
        self.assertEqual(sort_array([0]), [0])

    def test_sort_array_with_large_numbers(self):
        self.assertEqual(sort_array([1000000, 1000001, 1000002]), [1000000, 1000001, 1000002])

if __name__ == '__main__':
    unittest.main()


This test suite covers a variety of cases for the `sort_array` function, including positive integers, negative integers, mixed integers (including zero), empty lists, single-element lists, lists with duplicate elements, and lists with large numbers. Each test case checks that the output of `sort_array` matches the expected sorted list according to the rules specified in the function's docstring.