Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

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

 import unittest
from HumanEval_21_code import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):

    def test_rescale_to_unit_with_valid_input(self):
        # Test with a list of floats
        input_numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

    def test_rescale_to_unit_with_empty_list(self):
        # Test with an empty list
        input_numbers = []
        expected_output = []
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

    def test_rescale_to_unit_with_single_element(self):
        # Test with a list containing only one element
        input_numbers = [10.0]
        expected_output = [1.0]
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

    def test_rescale_to_unit_with_all_same_elements(self):
        # Test with a list containing all the same elements
        input_numbers = [5.0, 5.0, 5.0, 5.0, 5.0]
        expected_output = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

    def test_rescale_to_unit_with_negative_numbers(self):
        # Test with a list containing negative numbers
        input_numbers = [-1.0, -2.0, -3.0, -4.0, -5.0]
        expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

    def test_rescale_to_unit_with_zero_max_value(self):
        # Test with a list where the maximum value is zero
        input_numbers = [0.0, 0.0, 0.0, 0.0, 0.0]
        expected_output = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

if __name__ == '__main__':
    unittest.main()