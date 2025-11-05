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
    return l

 Here is a unittest test script for the `sort_third` function:


import unittest
from HumanEval_33_code import sort_third

class TestSortThird(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_third([]), [])

    def test_single_element_list(self):
        self.assertEqual(sort_third([1]), [1])

    def test_list_with_one_third_element(self):
        self.assertEqual(sort_third([1, 2, 3]), [1, 2, 3])

    def test_list_with_two_third_elements(self):
        self.assertEqual(sort_third([5, 6, 3]), [3, 6])

    def test_list_with_three_third_elements(self):
        self.assertEqual(sort_third([5, 6, 3, 4]), [3, 4, 5, 6])

    def test_list_with_more_than_three_third_elements(self):
        self.assertEqual(sort_third([5, 6, 3, 4, 8, 9, 2]), [2, 6, 3, 4, 8, 9])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases for different scenarios, such as an empty list, a single-element list, a list with one, two, three, and more than three third elements. The test cases use the `assertEqual` method to compare the expected output with the actual output of the `sort_third` function.