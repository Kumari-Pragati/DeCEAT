user

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
    return [n for n in numbers if c[n] <= 1]assistant

Here is the unittest test script for the `remove_duplicates` function:

import unittest
from HumanEval_26_code import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_duplicates([1]), [1])

    def test_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_duplicates_with_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 4]), [1, 2, 4])

    def test_duplicates_with_duplicates_and_order_matters(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 3, 4, 2, 1]), [1, 2, 4])

    def test_duplicates_with_duplicates_and_order_matters_and_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 4, 4, 1, 2]), [1, 2, 4])

    def test_duplicates_with_duplicates_and_order_matters_and_duplicates_and_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 4, 4, 1, 2, 3, 3]), [1, 2, 4])

if __name__ == '__main__':
    unittest.main()

This script tests the `remove_duplicates` function with various inputs, including:

* An empty list
* A list with a single element
* A list with duplicates
* A list with duplicates and order matters
* A list with duplicates, order matters, and duplicates again
* A list with duplicates, order matters, duplicates again, and duplicates again

Each test case checks that the output of the `remove_duplicates` function is correct.