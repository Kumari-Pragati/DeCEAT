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

 Here is a unittest test script for the `remove_duplicates` function:


import unittest
from HumanEval_26_code import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])
        self.assertEqual(remove_duplicates([2, 2, 3, 3, 4]), [2, 3, 4])
        self.assertEqual(remove_duplicates([1, 1, 1, 1, 2]), [2])
        self.assertEqual(remove_duplicates([]), [])
        self.assertEqual(remove_duplicates([1]), [1])
        self.assertEqual(remove_duplicates([1, 1, 1]), [1])
        self.assertEqual(remove_duplicates([1, 1, 1, 1, 1]), [1])
        self.assertEqual(remove_duplicates([-1, 0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 3]), [-1, 0, 1, 2])

if __name__ == '__main__':
    unittest.main()


This test script includes several test cases to cover different scenarios, such as empty lists, single elements, multiple elements, duplicates, and negative numbers. It uses the `assertEqual` method to check if the expected output matches the actual output produced by the `remove_duplicates` function.