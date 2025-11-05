system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return [n for n in numbers if c[n] <= 1]


assistant

import unittest

# Importing the function to be tested
from HumanEval_26_code import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        # Test case 1: Basic usage
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

        # Test case 2: Single element
        self.assertEqual(remove_duplicates([5]), [5])

        # Test case 3: All unique elements
        self.assertEqual(remove_duplicates([]), [])

        # Test case 4: Multiple duplicates
        self.assertEqual(remove_duplicates([1, 1, 1, 2, 3, 3, 3, 4]), [1, 2, 4])

        # Test case 5: Duplicates at both ends
        self.assertEqual(remove_duplicates([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), [10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

        # Test case 6: Empty list
        self.assertEqual(remove_duplicates([]), [])

        # Test case 7: Mixed duplicates and non-duplicates
        self.assertEqual(remove_duplicates([1, 1, 2, 3, 3, 4, 5, 5, 6]), [1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()


This script imports the `remove_duplicates` function and defines several test cases using the `assertEqual` method to verify its correctness across various scenarios. The `unittest.main()` call ensures that the tests can be run directly when this file is executed.