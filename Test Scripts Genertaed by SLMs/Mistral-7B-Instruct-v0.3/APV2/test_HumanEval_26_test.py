You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
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

 Here is the complete unittest test suite for the `remove_duplicates` function:


import unittest
from HumanEval_26_code import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_single_element(self):
        self.assertEqual(remove_duplicates([1]), [1])

    def test_single_duplicate(self):
        self.assertEqual(remove_duplicates([1, 1]), [1])

    def test_multiple_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 2, 4]), [1, 3, 4])

    def test_duplicates_at_beginning_and_end(self):
        self.assertEqual(remove_duplicates([2, 2, 1, 1, 2]), [1])

    def test_duplicates_in_middle(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 2, 4, 2, 1]), [1, 3, 4])

    def test_duplicates_with_unique_elements(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 1, 2, 3, 4]), [1, 2, 3, 4])

    def test_duplicates_with_only_duplicates(self):
        self.assertEqual(remove_duplicates([2, 2, 2, 2]), [])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as an empty list, single elements, multiple duplicates, duplicates at the beginning and end, duplicates in the middle, duplicates with unique elements, and duplicates with only duplicates.