You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a simple unittest test suite for the `truncate_number` function. I've included a few test cases to cover different scenarios:


import unittest
from HumanEval_2_code import truncate_number

class TestTruncateNumber(unittest.TestCase):
    def test_truncate_number(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5)
        self.assertAlmostEqual(truncate_number(0.5), 0.0)
        self.assertAlmostEqual(truncate_number(7.0), 0.0)
        self.assertAlmostEqual(truncate_number(-3.5), -0.5)
        self.assertAlmostEqual(truncate_number(0.0), 0.0)
        self.assertRaises(TypeError, truncate_number, "not a number")

if __name__ == '__main__':
    unittest.main()


This test suite includes a test case for a positive number, a test case for a zero number, a test case for a negative number, and a test case for a non-number input. The `assertAlmostEqual` function is used to compare the floating-point numbers with a tolerance, and the `assertRaises` function is used to test for exceptions.