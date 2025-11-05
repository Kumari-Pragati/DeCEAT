You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_13_code import greatest_common_divisor
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    while b:
        a, b = b, a % b
    return a


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_13_code import greatest_common_divisor

class TestGreatestCommonDivisor(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(greatest_common_divisor(25, 15), 5)
        self.assertEqual(greatest_common_divisor(3, 5), 1)

    def test_negative_numbers(self):
        self.assertEqual(greatest_common_divisor(-25, -15), 5)
        self.assertEqual(greatest_common_divisor(-3, -5), 1)

    def test_mixed_numbers(self):
        self.assertEqual(greatest_common_divisor(-25, 15), 5)
        self.assertEqual(greatest_common_divisor(3, -5), 1)

    def test_zero(self):
        self.assertEqual(greatest_common_divisor(0, 15), 15)
        self.assertEqual(greatest_common_divisor(3, 0), 3)
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            greatest_common_divisor(25, '15')
        with self.assertRaises(TypeError):
            greatest_common_divisor('25', 15)
        with self.assertRaises(TypeError):
            greatest_common_divisor('25', '15')

if __name__ == '__main__':
    unittest.main()


This script includes tests for positive numbers, negative numbers, mixed numbers, zero, and invalid input. It checks if the function returns the correct greatest common divisor for each case. If the function does not return the correct result, the test will fail.

Please note that you need to have the function `greatest_common_divisor` defined in a file named `HumanEval_13_code.py` for these tests to work.