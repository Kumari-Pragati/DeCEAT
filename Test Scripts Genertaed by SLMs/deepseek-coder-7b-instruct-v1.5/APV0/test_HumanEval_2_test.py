You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_2_code import truncate_number

class TestTruncateNumber(unittest.TestCase):

    def test_positive_floats(self):
        self.assertAlmostEqual(truncate_number(3.5), 0.5)
        self.assertAlmostEqual(truncate_number(1.23456), 0.23456)
        self.assertAlmostEqual(truncate_number(0.1), 0.1)

    def test_negative_floats(self):
        self.assertAlmostEqual(truncate_number(-3.5), 0.5)
        self.assertAlmostEqual(truncate_number(-1.23456), 0.76544)
        self.assertAlmostEqual(truncate_number(-0.1), 0.9)

    def test_integers(self):
        self.assertAlmostEqual(truncate_number(3), 0)
        self.assertAlmostEqual(truncate_number(-3), 0)

    def test_zero(self):
        self.assertAlmostEqual(truncate_number(0), 0)

if __name__ == '__main__':
    unittest.main()


This script tests the truncate_number function with positive floats, negative floats, integers, and zero. It uses the assertAlmostEqual method to compare the output of the function with the expected result.

Please note that the truncate_number function should be in a file named HumanEval_2_code.py in the same directory as this unittest script for the script to work correctly.