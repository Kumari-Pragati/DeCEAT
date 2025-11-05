user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_9_code import rolling_max
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """Return a list where each element is the maximum of all elements up to that index.
    >>> rolling_max([1, 2, 3, 2, 5])
    [1, 2, 3, 3, 5]
    >>> rolling_max([])
    []
    """
    result: List[int] = []
    running_max = None
    for n in numbers:
        if running_max is None:
            running_max = n
        else:
            running_max = max(running_max, n)
        result.append(running_max)
    return resultassistant

Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_9_code import rolling_max

class TestRollingMax(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(rolling_max([]), [])

    def test_single_element_list(self):
        self.assertEqual(rolling_max([1]), [1])

    def test_single_element_list_with_negative_number(self):
        self.assertEqual(rolling_max([-1]), [-1])

    def test_list_with_multiple_elements(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 5]), [1, 2, 3, 3, 5])

    def test_list_with_negative_numbers(self):
        self.assertEqual(rolling_max([-1, -2, -3, -2, -5]), [-1, -2, -3, -3, -5])

    def test_list_with_positive_and_negative_numbers(self):
        self.assertEqual(rolling_max([1, -2, 3, -4, 5]), [1, -2, 3, 3, 5])

    def test_list_with_duplicates(self):
        self.assertEqual(rolling_max([1, 2, 2, 3, 3, 3]), [1, 2, 2, 3, 3, 3])

    def test_list_with_negative_duplicates(self):
        self.assertEqual(rolling_max([-1, -2, -2, -3, -3, -3]), [-1, -2, -2, -3, -3, -3])

    def test_list_with_positive_and_negative_duplicates(self):
        self.assertEqual(rolling_max([1, -2, -2, 3, -3, -3]), [1, -2, -2, 3, 3, 3])

if __name__ == '__main__':
    unittest.main()


This test suite covers a variety of test cases, including:

* An empty list
* A list with a single element
* A list with multiple elements
* A list with negative numbers
* A list with positive and negative numbers
* A list with duplicates
* A list with negative duplicates
* A list with positive and negative duplicates

Each test case checks that the output of the `rolling_max` function is as expected.