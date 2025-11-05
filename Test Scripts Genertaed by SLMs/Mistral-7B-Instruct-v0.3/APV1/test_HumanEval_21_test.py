You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_21_code import rescale_to_unit

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1.
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number - min_number) for x in numbers]

 Here is a comprehensive unittest test suite for the `rescale_to_unit` function:


import unittest
from HumanEval_21_code import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(rescale_to_unit([]), [])

    def test_single_element(self):
        self.assertListEqual(rescale_to_unit([0]), [0])
        self.assertListEqual(rescale_to_unit([1]), [1])
        self.assertListEqual(rescale_to_unit([-1]), [0])

    def test_two_elements(self):
        self.assertListEqual(rescale_to_unit([0, 1]), [0, 1])
        self.assertListEqual(rescale_to_unit([1, 0]), [1, 0])
        self.assertListEqual(rescale_to_unit([-1, 0]), [1, 0])
        self.assertListEqual(rescale_to_unit([0, -1]), [0, 1])

    def test_multiple_elements(self):
        self.assertListEqual(rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0]), [0.0, 0.25, 0.5, 0.75, 1.0])
        self.assertListEqual(rescale_to_unit([-5.0, -4.0, -3.0, -2.0, -1.0]), [1.0, 0.75, 0.5, 0.25, 0])
        self.assertListEqual(rescale_to_unit([0.1, 0.2, 0.3, 0.4, 0.5]), [0.0, 0.04, 0.08, 0.16, 0.33])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for empty lists, single elements, two elements, and multiple elements. It covers various edge cases, such as negative numbers, and tests the function with different ranges of numbers.