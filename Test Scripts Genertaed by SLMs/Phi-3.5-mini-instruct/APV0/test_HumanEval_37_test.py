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

 import unittest
from HumanEval_37_code import sort_even

class TestSortEven(unittest.TestCase):

    def test_sort_even_identity_preserved(self):
        self.assertEqual(sort_even([1, 2, 3]), [1, 2, 3])

    def test_sort_even_maintains_odd_indices(self):
        self.assertEqual(sort_even([5, 6, 3, 4]), [3, 6, 5, 4])

    def test_sort_even_with_even_indices_sorted(self):
        self.assertEqual(sort_even([4, 1, 3, 2]), [1, 2, 3, 4])

    def test_sort_even_with_uneven_lengths(self):
        self.assertEqual(sort_even([1, 3, 5]), [1, 3, 5])

    def test_sort_even_with_empty_list(self):
        self.assertEqual(sort_even([]), [])

    def test_sort_even_with_single_element(self):
        self.assertEqual(sort_even([2]), [2])

    def test_sort_even_with_all_even_elements(self):
        self.assertEqual(sort_even([2, 4, 6]), [2, 4, 6])

    def test_sort_even_with_all_odd_elements(self):
        self.assertEqual(sort_even([1, 3, 5]), [1, 3, 5])

    def test_sort_even_with_mixed_elements(self):
        self.assertEqual(sort_even([5, 2, 3, 1]), [1, 2, 3, 5])

if __name__ == '__main__':
    unittest.main()