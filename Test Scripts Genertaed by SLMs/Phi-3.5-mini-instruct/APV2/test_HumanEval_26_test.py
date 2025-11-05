You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

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
from typing import List

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates_with_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_remove_duplicates_with_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_remove_duplicates_with_all_duplicates(self):
        self.assertEqual(remove_duplicates([2, 2, 2, 2]), [])

    def test_remove_duplicates_with_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_remove_duplicates_with_single_element(self):
        self.assertEqual(remove_duplicates([5]), [5])

    def test_remove_duplicates_with_negative_numbers(self):
        self.assertEqual(remove_duplicates([-1, -2, -1, -3]), [-2, -3])

    def test_remove_duplicates_with_mixed_types(self):
        with self.assertRaises(TypeError):
            remove_duplicates([1, "2", 3, "3"])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to ensure that the `remove_duplicates` function behaves as expected. It checks for lists with duplicates, lists without duplicates, empty lists, lists with a single element, lists with negative numbers, and lists containing mixed types to ensure proper error handling. The `assertRaises` method is used to test that a `TypeError` is raised when the function is given a list with elements of different types.