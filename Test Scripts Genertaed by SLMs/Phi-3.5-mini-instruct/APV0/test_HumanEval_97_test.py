Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_97_code import multiply
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.

    Examples:
    multiply(148, 412) ➞ 16
    multiply(19, 28) ➞ 72
    multiply(2020, 1851) ➞ 0
    multiply(14, -15) ➞ 20
    """

    return abs(a % 10) * abs(b % 10)

 import unittest
from HumanEval_97_code import multiply

class TestMultiplyFunction(unittest.TestCase):

    def test_multiply_with_positive_numbers(self):
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)
        self.assertEqual(multiply(2020, 1851), 0)

    def test_multiply_with_negative_numbers(self):
        self.assertEqual(multiply(14, -15), 20)

    def test_multiply_with_zero(self):
        self.assertEqual(multiply(0, 123), 0)
        self.assertEqual(multiply(123, 0), 0)

    def test_multiply_with_single_digit_numbers(self):
        self.assertEqual(multiply(5, 5), 25)
        self.assertEqual(multiply(7, 3), 21)

    def test_multiply_with_large_numbers(self):
        self.assertEqual(multiply(123456789, 987654321), 81)
        self.assertEqual(multiply(999999999, 999999999), 81)

    def test_multiply_with_zero_unit_digit(self):
        self.assertEqual(multiply(100, 200), 0)
        self.assertEqual(multiply(1234, 5000), 0)

    def test_multiply_with_negative_unit_digit(self):
        self.assertEqual(multiply(-100, 200), 0)
        self.assertEqual(multiply(1234, -5000), 0)

if __name__ == '__main__':
    unittest.main()