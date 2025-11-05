You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_26_code import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])
        self.assertEqual(remove_duplicates([1, 1, 1, 1]), [1])
        self.assertEqual(remove_duplicates([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(remove_duplicates([]), [])
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 3, 4]), [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for various scenarios:

1. When there are duplicates in the list.
2. When all elements are unique.
3. When there are no elements in the list.
4. When all elements are unique, but the list is not sorted.
5. When the list is already sorted.

Each test case checks that the output of the `remove_duplicates` function matches the expected result.