You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function `greatest_common_divisor`. The test cases cover a range of inputs to ensure the function works correctly.


import unittest
from HumanEval_13_code import greatest_common_divisor

class TestGCD(unittest.TestCase):

    def test_gcd_positive_numbers(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)
        self.assertEqual(greatest_common_divisor(25, 15), 5)
        self.assertEqual(greatest_common_divisor(49, 78), 7)
        self.assertEqual(greatest_common_divisor(123456789, 987654321), 72576360)

    def test_gcd_zero(self):
        self.assertEqual(greatest_common_divisor(0, 5), 0)
        self.assertEqual(greatest_common_divisor(5, 0), 0)

    def test_gcd_negative_numbers(self):
        self.assertEqual(greatest_common_divisor(-3, 5), 1)
        self.assertEqual(greatest_common_divisor(-25, -15), 5)
        self.assertEqual(greatest_common_divisor(-49, -78), 7)
        self.assertEqual(greatest_common_divisor(-123456789, -987654321), 72576360)

    def test_gcd_one(self):
        self.assertEqual(greatest_common_divisor(1, 1), 1)

    def test_gcd_large_numbers(self):
        self.assertEqual(greatest_common_divisor(1234567890123456789, 9876543210987654321), 4569876543210)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive numbers, zero, negative numbers, one, and large numbers. It covers a wide range of inputs to ensure the function works correctly.