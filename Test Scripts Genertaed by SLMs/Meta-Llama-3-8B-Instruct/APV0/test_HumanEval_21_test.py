user

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
    return [(x - min_number) / (max_number - min_number) for x in numbers]assistant

Here is the unittest test script for the `rescale_to_unit` function:

import unittest
from HumanEval_21_code import rescale_to_unit

class TestRescaleToUnit(unittest.TestCase):
    def test_rescale_to_unit(self):
        # Test with a simple list of numbers
        numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(numbers), expected_result)

        # Test with a list of numbers with negative values
        numbers = [-1.0, -2.0, -3.0, -4.0, -5.0]
        expected_result = [0.0, 0.25, 0.5, 0.75, 1.0]
        self.assertEqual(rescale_to_unit(numbers), expected_result)

        # Test with a list of numbers with zero values
        numbers = [0.0, 1.0, 2.0, 3.0, 4.0]
        expected_result = [0.0, 0.3333333333333333, 0.6666666666666666, 1.0]
        self.assertEqual(rescale_to_unit(numbers), expected_result)

        # Test with a list of numbers with duplicate values
        numbers = [1.0, 1.0, 2.0, 3.0, 4.0]
        expected_result = [0.0, 0.0, 0.3333333333333333, 0.6666666666666666, 1.0]
        self.assertEqual(rescale_to_unit(numbers), expected_result)

        # Test with an empty list
        numbers = []
        with self.assertRaises(ZeroDivisionError):
            rescale_to_unit(numbers)

        # Test with a list of non-numeric values
        numbers = [1, 2, 3, 4, 5]
        with self.assertRaises(TypeError):
            rescale_to_unit(numbers)

if __name__ == '__main__':
    unittest.main()

This test script covers the following scenarios:

1. A simple list of numbers with a range of values.
2. A list of numbers with negative values.
3. A list of numbers with zero values.
4. A list of numbers with duplicate values.
5. An empty list (which should raise a `ZeroDivisionError`).
6. A list of non-numeric values (which should raise a `TypeError`).

Note that the `assertEqual` method is used to compare the expected result with the actual result of the `rescale_to_unit` function. The `assertRaises` method is used to verify that the expected exception is raised when the input is invalid.