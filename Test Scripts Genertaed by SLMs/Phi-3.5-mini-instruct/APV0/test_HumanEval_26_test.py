Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

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
    return [n for n in numbers if c[n] <= 1]

 import unittest
from HumanEval_26_code import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_remove_duplicates_single_element(self):
        self.assertEqual(remove_duplicates([1]), [1])

    def test_remove_duplicates_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_remove_duplicates_all_duplicates(self):
        self.assertEqual(remove_duplicates([2, 2, 2, 2]), [])

    def test_remove_duplicates_with_order_preserved(self):
        self.assertEqual(remove_duplicates([1, 3, 2, 3, 4]), [1, 2, 4])

    def test_remove_duplicates_with_mixed_integers(self):
        self.assertEqual(remove_duplicates([5, -1, 0, 5, -1, 0]), [-1, 0])

    def test_remove_duplicates_with_negative_numbers(self):
        self.assertEqual(remove_duplicates([-1, -2, -3, -2, -1]), [-3])

    def test_remove_duplicates_with_large_numbers(self):
        self.assertEqual(remove_duplicates([1000000, 2000000, 3000000, 2000000]), [1000000, 3000000])

if __name__ == '__main__':
    unittest.main()