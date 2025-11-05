You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_mean_absolute_deviation_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0)

    def test_mean_absolute_deviation_single_element(self):
        self.assertEqual(mean_absolute_deviation([5]), 0)

    def test_mean_absolute_deviation_identical_elements(self):
        self.assertEqual(mean_absolute_deviation([2.0, 2.0, 2.0, 2.0]), 0)

    def test_mean_absolute_deviation_integers(self):
        self.assertAlmostEqual(mean_absolute_deviation([1, 2, 3, 4]), 1.0)

    def test_mean_absolute_deviation_floats(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    def test_mean_absolute_deviation_negative_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, -2.0, -3.0, -4.0]), 1.0)

    def test_mean_absolute_deviation_mixed_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([1, 2.5, 3, 4.5]), 1.0)

    def test_mean_absolute_deviation_large_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([1000, 2000, 3000, 4000]), 1000.0)

    def test_mean_absolute_deviation_zero_mean(self):
        self.assertAlmostEqual(mean_absolute_deviation([0, 0, 0, 0]), 0)

    def test_mean_absolute_deviation_rational_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([1/2, 2/3, 3/4, 4/5]), 0.05)

    def test_mean_absolute_deviation_random_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.1, 2.2, 3.3, 4.4]), 1.1)

if __name__ == '__main__':
    unittest.main()