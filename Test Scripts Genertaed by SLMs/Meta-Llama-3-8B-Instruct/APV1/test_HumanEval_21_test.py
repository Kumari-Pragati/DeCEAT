user

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
    return [(x - min_number) / (max_number - min_number) for x in numbers]assistant

Here is a comprehensive unittest test suite for the `rescale_to_unit` function:


import unittest
from HumanEval_21_code import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):

    def test_rescale_to_unit_with_valid_input(self):
        # Test with a list of numbers
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(numbers), expected_output)

    def test_rescale_to_unit_with_empty_list(self):
        # Test with an empty list
        numbers = []
        with self.assertRaises(ZeroDivisionError):
            rescale_to_unit(numbers)

    def test_rescale_to_unit_with_single_element_list(self):
        # Test with a list containing a single element
        numbers = [1.0]
        expected_output = [0.0]
        self.assertEqual(rescale_to_unit(numbers), expected_output)

    def test_rescale_to_unit_with_all_equal_elements(self):
        # Test with a list containing all equal elements
        numbers = [1.0, 1.0, 1.0, 1.0, 1.0]
        expected_output = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.assertEqual(rescale_to_unit(numbers), expected_output)

    def test_rescale_to_unit_with_negative_numbers(self):
        # Test with a list containing negative numbers
        numbers = [-1.0, -2.0, -3.0, -4.0, -5.0]
        expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(numbers), expected_output)

    def test_rescale_to_unit_with_mixed_positive_and_negative_numbers(self):
        # Test with a list containing both positive and negative numbers
        numbers = [-1.0, -2.0, 1.0, 2.0, 3.0]
        expected_output = [-1.0, -0.5, 0.0, 0.5, 1.0]
        self.assertEqual(rescale_to_unit(numbers), expected_output)

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios, including:

* Testing with a valid list of numbers
* Testing with an empty list
* Testing with a list containing a single element
* Testing with a list containing all equal elements
* Testing with a list containing negative numbers
* Testing with a list containing both positive and negative numbers

Each test case checks the output of the `rescale_to_unit` function against the expected output, and uses assertions to verify that the output is correct.