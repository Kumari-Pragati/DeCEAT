user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_26_code import remove_duplicates
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    import collections
    c = collections.Counter(numbers)
    return [n for n in numbers if c[n] <= 1]assistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_26_code import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates(self):
        # Test case 1: List with no duplicates
        self.assertEqual(remove_duplicates([1, 2, 3, 4]), [1, 2, 3, 4])

        # Test case 2: List with duplicates
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

        # Test case 3: List with duplicates in different orders
        self.assertEqual(remove_duplicates([4, 2, 3, 1, 2]), [4, 1, 3])

        # Test case 4: List with duplicates in different orders and different lengths
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4, 4, 5, 6, 6]), [1, 2, 3, 4, 5, 6])

        # Test case 5: List with all duplicates
        self.assertEqual(remove_duplicates([1, 1, 1, 1]), [])

        # Test case 6: List with no duplicates and no elements
        self.assertEqual(remove_duplicates([]), [])

        # Test case 7: List with no duplicates and one element
        self.assertEqual(remove_duplicates([1]), [1])

        # Test case 8: List with no duplicates and two elements
        self.assertEqual(remove_duplicates([1, 2]), [1, 2])

        # Test case 9: List with duplicates and no elements
        self.assertEqual(remove_duplicates([1, 1]), [])

        # Test case 10: List with duplicates and one element
        self.assertEqual(remove_duplicates([1, 1, 1]), [])

        # Test case 11: List with duplicates and two elements
        self.assertEqual(remove_duplicates([1, 1, 2, 2]), [1, 2])

        # Test case 12: List with duplicates and three elements
        self.assertEqual(remove_duplicates([1, 1, 2, 2, 3, 3]), [1, 2, 3])

        # Test case 13: List with duplicates and four elements
        self.assertEqual(remove_duplicates([1, 1, 2, 2, 3, 3, 4, 4]), [1, 2, 3, 4])

        # Test case 14: List with duplicates and five elements
        self.assertEqual(remove_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), [1, 2, 3, 4, 5])

        # Test case 15: List with duplicates and six elements
        self.assertEqual(remove_duplicates([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]), [1, 2, 3, 4, 5, 6])

    def test_remove_duplicates_edge_cases(self):
        # Test case 16: List with duplicates and negative numbers
        self.assertEqual(remove_duplicates([-1, -1, 0, 0, 1, 1]), [-1, 0, 1])

        # Test case 17: List with duplicates and zero
        self.assertEqual(remove_duplicates([0, 0, 1, 1]), [0, 1])

        # Test case 18: List with duplicates and negative numbers and zero
        self.assertEqual(remove_duplicates([-1, -1, 0, 0, 1, 1]), [-1, 0, 1])

        # Test case 19: List with duplicates and negative numbers and zero and duplicates
        self.assertEqual(remove_duplicates([-1, -1, 0, 0, 1, 1, 2, 2]), [-1, 0, 1, 2])

        # Test case 20: List with duplicates and negative numbers and zero and duplicates and negative numbers
        self.assertEqual(remove_duplicates([-1, -1, 0, 0, 1, 1, 2, 2, -2, -2]), [-1, 0, 1, 2])

if __name__ == '__main__':
    unittest.main()


This test suite includes 20 test cases to cover various scenarios, including lists with no duplicates, lists with duplicates, lists with duplicates in different orders, lists with all duplicates, and edge cases such as lists with negative numbers and zero.