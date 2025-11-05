You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_4_code import mean_absolute_deviation

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_mean_absolute_deviation(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)
        self.assertAlmostEqual(mean_absolute_deviation([10.0, 20.0, 30.0, 40.0]), 15.0)
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0]), 0.6666666666666666)
        self.assertAlmostEqual(mean_absolute_deviation([10.0]), 0.0)
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]), 1.4)

if __name__ == '__main__':
    unittest.main()


This test suite includes five test cases, each testing the `mean_absolute_deviation` function with a different input list of numbers. The `assertAlmostEqual` method is used to compare the expected and actual results, allowing for a small difference due to floating-point precision issues.

Please note that the `HumanEval_4_code` module should contain the `mean_absolute_deviation` function for these tests to pass. If the function is defined in a different module, you should replace `HumanEval_4_code` with the correct module name.