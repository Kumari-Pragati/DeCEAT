system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return sum(abs(x - mean) for x in numbers) / len(numbers)


assistant

import unittest

# Importing the function to be tested
from HumanEval_4_code import mean_absolute_deviation

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)

    def test_single_element(self):
        self.assertAlmostEqual(mean_absolute_deviation([5]), 0.0)

    def test_uniform_list(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 0.5)

    def test_mixed_values(self):
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, 0.0, 1.0]), 0.6666666666666666)

    def test_large_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([1e9, 2e9, 3e9, 4e9]), 1.5e9)

if __name__ == '__main__':
    unittest.main()


This script imports the `mean_absolute_deviation` function and creates a class `TestMeanAbsoluteDeviation` that inherits from `unittest.TestCase`. It includes several test cases to ensure the function behaves as expected under different conditions. The `assertAlmostEqual` method is used for floating-point comparisons to account for potential rounding errors.