Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_37_code import sort_even
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    evens = l[::2]
    odds = l[1::2]
    evens.sort()
    ans = []
    for e, o in zip(evens, odds):
        ans.extend([e, o])
    if len(evens) > len(odds):
        ans.append(evens[-1])
    return ans

 Here is a unittest test script for the `sort_even` function:


import unittest
from HumanEval_37_code import sort_even

class TestSortEven(unittest.TestCase):

    def test_sort_even_empty_list(self):
        self.assertEqual(sort_even([]), [])

    def test_sort_even_single_element_list(self):
        self.assertEqual(sort_even([1]), [1])

    def test_sort_even_even_length_list(self):
        self.assertEqual(sort_even([5, 6]), [5, 6])

    def test_sort_even_odd_length_list(self):
        self.assertEqual(sort_even([5, 6, 3]), [3, 6, 5])

    def test_sort_even_list_with_duplicates(self):
        self.assertEqual(sort_even([5, 6, 3, 6]), [3, 6, 6, 5])

    def test_sort_even_list_with_unsorted_evens(self):
        self.assertEqual(sort_even([5, 3, 6, 4]), [3, 6, 4, 5])

    def test_sort_even_list_with_longer_evens(self):
        self.assertEqual(sort_even([5, 6, 3, 4, 7]), [3, 6, 4, 7, 5])

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases to ensure the function works correctly for different input scenarios. It covers empty lists, single-element lists, lists with even and odd lengths, lists with duplicates, lists with unsorted evens, and lists where the evens have a longer length than the odds.