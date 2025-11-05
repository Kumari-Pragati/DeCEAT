user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_30_code import get_positive
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    return [e for e in l if e > 0]assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_30_code import get_positive

class TestGetPositive(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(get_positive([2, 5, 6]), [2, 5, 6])

    def test_negative_numbers(self):
        self.assertEqual(get_positive([-1, -4, -5, -3, -10]), [])

    def test_mixed_numbers(self):
        self.assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]), [5, 3, 2, 3, 9, 123, 1])

    def test_empty_list(self):
        self.assertEqual(get_positive([]), [])

    def test_single_element_list(self):
        self.assertEqual(get_positive([5]), [5])

    def test_list_with_zero(self):
        self.assertEqual(get_positive([5, 0, 3, 2, -3, 9, 123, 1, -10]), [5, 3, 2, 9, 123, 1])

    def test_list_with_duplicates(self):
        self.assertEqual(get_positive([5, 5, 3, 2, 2, -3, 9, 123, 1, -10]), [5, 5, 3, 2, 2, 9, 123, 1])

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios, including:

- Testing with only positive numbers
- Testing with only negative numbers
- Testing with a mix of positive and negative numbers
- Testing with an empty list
- Testing with a single-element list
- Testing with a list containing zero
- Testing with a list containing duplicate positive numbers