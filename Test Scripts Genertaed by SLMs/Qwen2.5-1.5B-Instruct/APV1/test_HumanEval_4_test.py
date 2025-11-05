system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Importing the function we want to test
from HumanEval_4_code import mean_absolute_deviation

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(mean_absolute_deviation([]), 0.0)

    def test_single_element(self):
        self.assertAlmostEqual(mean_absolute_deviation([5.0]), 0.0)

    def test_uniform_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)

    def test_mixed_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([-1.0, 0.0, 1.0]), 0.6666666666666666)

    def test_large_numbers(self):
        self.assertAlmostEqual(mean_absolute_deviation([100.0, 200.0, 300.0, 400.0]), 150.0)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestMeanAbsoluteDeviation` class that inherits from `unittest.TestCase`. It contains several test methods to verify the correctness of the `mean_absolute_deviation` function. The tests cover various scenarios including empty lists, single-element lists, uniformly distributed numbers, mixed numbers, and large numbers. Each method uses assertions to check if the output matches the expected value or calculates it correctly using the provided formula.