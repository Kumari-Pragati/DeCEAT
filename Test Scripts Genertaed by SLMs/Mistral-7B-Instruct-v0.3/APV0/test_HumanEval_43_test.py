Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_43_code import pairs_sum_to_zero
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    It returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    for i, l1 in enumerate(l):
        for j in range(i + 1, len(l)):
            if l1 + l[j] == 0:
                return True
    return False

 Here is a unittest test script for the provided function `pairs_sum_to_zero`. The test cases cover various scenarios, including empty lists, lists with only one element, lists with duplicate elements, and lists with pairs that sum to zero.


import unittest
from HumanEval_43_code import pairs_sum_to_zero

class TestPairsSumToZero(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(pairs_sum_to_zero([]))

    def test_list_with_one_element(self):
        self.assertFalse(pairs_sum_to_zero([1]))
        self.assertFalse(pairs_sum_to_zero([-1]))

    def test_list_with_duplicates(self):
        self.assertFalse(pairs_sum_to_zero([1, 1, 3, 5]))
        self.assertFalse(pairs_sum_to_zero([-1, -1, -2, 1]))

    def test_list_with_pairs_that_sum_to_zero(self):
        self.assertTrue(pairs_sum_to_zero([1, 3, -2, 1]))
        self.assertTrue(pairs_sum_to_zero([2, 4, -5, 3, 5, 7]))
        self.assertTrue(pairs_sum_to_zero([-3, 3, -2, 2]))

if __name__ == '__main__':
    unittest.main()


This script includes a test case for an empty list, a test case for a list with one element, a test case for a list with duplicate elements, and a test case for a list with pairs that sum to zero. The test cases use the `assertFalse` and `assertTrue` methods provided by the `unittest.TestCase` class to verify the expected behavior of the `pairs_sum_to_zero` function.