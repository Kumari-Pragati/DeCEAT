system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

Here is the complete unittest test suite for the `rolling_max` function:


import unittest
from HumanEval_9_code import rolling_max

class TestRollingMax(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(rolling_max([]), [])

    def test_single_element_list(self):
        self.assertEqual(rolling_max([1]), [1])

    def test_single_element_list_with_negative_number(self):
        self.assertEqual(rolling_max([-1]), [-1])

    def test_multiple_elements_list(self):
        self.assertEqual(rolling_max([1, 2, 3, 2, 5]), [1, 2, 3, 3, 5])

    def test_multiple_elements_list_with_negative_numbers(self):
        self.assertEqual(rolling_max([-1, -2, -3, -2, -5]), [-1, -2, -3, -3, -5])

    def test_multiple_elements_list_with_duplicates(self):
        self.assertEqual(rolling_max([1, 2, 2, 3, 3, 3, 4, 5, 5, 5]), [1, 2, 2, 3, 3, 3, 4, 5, 5, 5])

    def test_multiple_elements_list_with_duplicates_and_negative_numbers(self):
        self.assertEqual(rolling_max([-1, -2, -2, -3, -3, -3, -4, -5, -5, -5]), [-1, -2, -2, -3, -3, -3, -4, -5, -5, -5])

if __name__ == '__main__':
    unittest.main()