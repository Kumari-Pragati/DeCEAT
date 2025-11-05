You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

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

 
import unittest
from HumanEval_4_code import mean_absolute_deviation
from typing import List

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_mean_absolute_deviation_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)

    def test_mean_absolute_deviation_single_element(self):
        self.assertEqual(mean_absolute_deviation([5.0]), 0.0)

    def test_mean_absolute_deviation_all_same_values(self):
        self.assertEqual(mean_absolute_deviation([2.0, 2.0, 2.0, 2.0]), 0.0)

    def test_mean_absolute_deviation_integers(self):
        self.assertAlmostEqual(mean_absolute_deviation([1, 2, 3, 4]), 1.0)

    def test_mean_absolute_deviation_floats(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    def test_mean_absolute_deviation_negative_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0]), 1.0)

    def test_mean_absolute_deviation_zero_numbers(self):
        self.assertEqual(mean_absolute_deviation([0.0, 0.0, 0.0, 0.0]), 0.0)

    def test_mean_absolute_deviation_mixed_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.5, 3.0, 4.5]), 1.0)

if __name__ == '__main__':
    unittest.main()


This test suite covers various scenarios for the `mean_absolute_deviation` function, including empty lists, single-element lists, lists with all identical values, lists with integers, lists with floating-point numbers, lists with negative numbers, lists with zero, and lists with a mix of numbers. The `assertAlmostEqual` method is used for floating-point comparisons to account for potential rounding errors.