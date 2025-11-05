user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_33_code import sort_third
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indices that are not divisible by three, while its values at the indices that are divisible by three are equal
    to the values of the corresponding indices of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    l = list(l)
    l[::3] = sorted(l[::3])
    return lassistant

Here is the unittest test script for the `sort_third` function:

import unittest
from HumanEval_33_code import sort_third

class TestSortThird(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(sort_third([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_third([1]), [1])

    def test_list_with_no_third_indices(self):
        self.assertEqual(sort_third([1, 2, 4]), [1, 2, 4])

    def test_list_with_third_indices(self):
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])

    def test_list_with_third_indices_and_sorted(self):
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9, 5])

    def test_list_with_third_indices_and_unsorted(self):
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 7]), [7, 6, 3, 4, 8, 9, 5])

    def test_list_with_duplicates(self):
        self.assertEqual(sort_third([1, 2, 3, 3, 4, 5, 6]), [1, 2, 3, 3, 4, 5, 6])

    def test_list_with_negative_numbers(self):
        self.assertEqual(sort_third([-1, -2, -3]), [-1, -2, -3])

if __name__ == '__main__':
    unittest.main()

This test script covers a variety of cases, including:

* An empty list
* A single-element list
* A list with no indices divisible by 3
* A list with indices divisible by 3, but no sorting required
* A list with indices divisible by 3, and sorting required
* A list with duplicates
* A list with negative numbers

Each test case uses the `assertEqual` method to verify that the output of the `sort_third` function matches the expected output.