You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_4_code import mean_absolute_deviation

class TestMeanAbsoluteDeviation(unittest.TestCase):

    def test_mean_absolute_deviation(self):
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]), 1.0)
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0, 5.0]), 1.2)
        self.assertAlmostEqual(mean_absolute_deviation([10.0, 20.0, 30.0, 40.0]), 15.0)
        self.assertAlmostEqual(mean_absolute_deviation([1.0, 2.0, 3.0]), 0.6666666666666666)
        self.assertAlmostEqual(mean_absolute_deviation([10.0, 20.0, 30.0]), 13.333333333333334)
        self.assertAlmostEqual(mean_absolute_deviation([1.0]), 0.0)
        self.assertAlmostEqual(mean_absolute_deviation([10.0]), 0.0)
        self.assertAlmostEqual(mean_absolute_deviation([]), 0.0)

if __name__ == '__main__':
    unittest.main()


This script creates a unittest class `TestMeanAbsoluteDeviation` that inherits from `unittest.TestCase`. Inside this class, there is a method `test_mean_absolute_deviation` that tests the `mean_absolute_deviation` function with different inputs. Each test checks if the output of the function matches the expected result.

The `assertAlmostEqual` method is used to compare the actual output of the function with the expected result. If they are not equal, the test will fail.

Finally, the script ends with `unittest.main()`, which runs all the tests when the script is run directly.