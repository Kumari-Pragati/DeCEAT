You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
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

 Here is a complete unittest test suite for the `mean_absolute_deviation` function:


import unittest
from HumanEval_4_code import mean_absolute_deviation

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_mean_absolute_deviation(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, 0.0, 1.0, 4.0]), 2.0)
        self.assertAlmostEqual(mean_absolute_deviation([2.0, 2.0, 2.0]), 0.0)
        self.assertAlmostEqual(mean_absolute_deviation([0.0]), 0.0)
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 1.0, 1.0]), 0.0)
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]), 1.3333333333333337)
        self.assertRaises(TypeError, mean_absolute_deviation, [1, 2, 3])
        self.assertRaises(TypeError, mean_absolute_deviation, [1.0, 2, 3.0])

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases to cover various scenarios, including edge cases and error handling. It uses the `assertAlmostEqual` method to compare the expected and actual results with a tolerance for floating-point errors. Additionally, it uses the `assertRaises` method to test error handling.