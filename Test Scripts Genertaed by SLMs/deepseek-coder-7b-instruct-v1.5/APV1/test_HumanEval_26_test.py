You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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
    return [n for n in numbers if c[n] <= 1]


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_26_code import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_single_element(self):
        self.assertEqual(remove_duplicates([1]), [1])

    def test_no_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_duplicates(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4]), [1, 3, 4])

    def test_duplicates_at_end(self):
        self.assertEqual(remove_duplicates([1, 2, 3, 2, 4]), [1, 3, 4])

    def test_duplicates_at_start(self):
        self.assertEqual(remove_duplicates([2, 2, 3, 4]), [2, 3, 4])

    def test_duplicates_in_middle(self):
        self.assertEqual(remove_duplicates([1, 2, 2, 3, 4, 2]), [1, 3, 4, 2])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for different scenarios such as an empty list, a list with a single element, a list with no duplicates, a list with duplicates, and a list with duplicates at the start, end, or in the middle.