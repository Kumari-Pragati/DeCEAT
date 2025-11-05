user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_4_code import mean_absolute_deviation
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a center point (mean in this case):
    MAD = average |x - x_mean|
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    mean = sum(numbers) / len(numbers)
    return sum(abs(x - mean) for x in numbers) / len(numbers)assistant

Here is a unittest test script for the `mean_absolute_deviation` function:

import unittest
from HumanEval_4_code import mean_absolute_deviation

class TestMeanAbsoluteDeviation(unittest.TestCase):
    def test_mean_absolute_deviation(self):
        # Test with a simple list of numbers
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

        # Test with a list of numbers with a mean of 0
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, 0.0, 1.0, 2.0]), 1.0)

        # Test with a list of numbers with a mean of 5
        self.assertAlmostEqual(mean_absolute_deviation([3.0, 4.0, 5.0, 6.0]), 1.0)

        # Test with an empty list
        self.assertAlmostEqual(mean_absolute_deviation([]), 0.0)

        # Test with a list of numbers with a mean of -5
        self.assertAlmostEqual(mean_absolute_deviation([-6.0, -5.0, -4.0, -3.0]), 1.0)

    def test_mean_absolute_deviation_edge_cases(self):
        # Test with a list of numbers with all identical values
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 1.0, 1.0, 1.0]), 0.0)

        # Test with a list of numbers with all identical values and a mean of 0
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, -1.0, -1.0, -1.0]), 0.0)

if __name__ == '__main__':
    unittest.main()

This script defines a `TestMeanAbsoluteDeviation` class with two test methods:

* `test_mean_absolute_deviation`: This method tests the `mean_absolute_deviation` function with various inputs, including a simple list of numbers, a list with a mean of 0, a list with a mean of 5, an empty list, and a list with a mean of -5.
* `test_mean_absolute_deviation_edge_cases`: This method tests the `mean_absolute_deviation` function with edge cases, including a list of numbers with all identical values and a list with all identical values and a mean of 0.

The `assertAlmostEqual` method is used to compare the results of the `mean_absolute_deviation` function with the expected results, with a small tolerance to account for floating-point precision errors.

You can run this script directly to execute the tests and verify that the `mean_absolute_deviation` function is working correctly.