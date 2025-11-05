Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_2_code import truncate_number
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def truncate_number(number: float) -> float:
    """Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number % 1.0

 Here is a simple unittest test script for the `truncate_number` function. The test cases cover various scenarios, including positive numbers, zero, and negative numbers.


import unittest
from HumanEval_2_code import truncate_number

class TestTruncateNumber(unittest.TestCase):
    def test_positive_number(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5)
        self.assertAlmostEqual(truncate_number(7.123), 0.123)
        self.assertAlmostEqual(truncate_number(1000.001), 0.001)

    def test_zero(self):
        self.assertAlmostEqual(truncate_number(0.0), 0.0)

    def test_negative_number(self):
        self.assertAlmostEqual(truncate_number(-3.5), 0.5)
        self.assertAlmostEqual(truncate_number(-7.123), 0.123)
        self.assertAlmostEqual(truncate_number(-1000.001), 0.001)

if __name__ == '__main__':
    unittest.main()


This script includes a test case for positive numbers, zero, and negative numbers. The `assertAlmostEqual` function is used to compare the expected and actual results with a tolerance for floating-point errors.