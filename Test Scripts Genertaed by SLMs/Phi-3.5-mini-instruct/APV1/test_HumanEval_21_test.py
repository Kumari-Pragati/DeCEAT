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

 import unittest
from HumanEval_21_code import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):

    def test_normal_case(self):
        """Test the function with a normal case where the list contains floats."""
        input_numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

    def test_empty_list(self):
        """Test the function with an empty list."""
        input_numbers = []
        expected_output = []
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

    def test_single_element_list(self):
        """Test the function with a list containing only one element."""
        input_numbers = [10.0]
        expected_output = [1.0]
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

    def test_all_elements_same(self):
        """Test the function with a list where all elements are the same."""
        input_numbers = [5.0, 5.0, 5.0, 5.0, 5.0]
        expected_output = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

    def test_negative_numbers(self):
        """Test the function with a list containing negative numbers."""
        input_numbers = [-1.0, -2.0, -3.0, -4.0, -5.0]
        expected_output = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

    def test_zero_max_value(self):
        """Test the function with a list where the maximum value is zero."""
        input_numbers = [0.0, 0.0, 0.0, 0.0, 0.0]
        expected_output = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.assertEqual(rescale_to_unit(input_numbers), expected_output)

if __name__ == '__main__':
    unittest.main()