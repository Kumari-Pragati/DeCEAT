user

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
    return aassistant

Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_13_code import greatest_common_divisor

class TestGreatestCommonDivisor(unittest.TestCase):

    def test_gcd_of_two_small_numbers(self):
        self.assertEqual(greatest_common_divisor(3, 5), 1)

    def test_gcd_of_two_large_numbers(self):
        self.assertEqual(greatest_common_divisor(25, 15), 5)

    def test_gcd_of_two_numbers_with_common_divisor(self):
        self.assertEqual(greatest_common_divisor(12, 15), 3)

    def test_gcd_of_two_numbers_with_no_common_divisor(self):
        self.assertEqual(greatest_common_divisor(7, 10), 1)

    def test_gcd_of_two_negative_numbers(self):
        self.assertEqual(greatest_common_divisor(-12, -15), 3)

    def test_gcd_of_two_positive_and_negative_numbers(self):
        self.assertEqual(greatest_common_divisor(12, -15), 3)

    def test_gcd_of_two_zero_numbers(self):
        self.assertEqual(greatest_common_divisor(0, 0), 0)

    def test_gcd_of_two_numbers_with_one_zero(self):
        self.assertEqual(greatest_common_divisor(0, 5), 5)

    def test_gcd_of_two_numbers_with_one_negative(self):
        self.assertEqual(greatest_common_divisor(0, -5), 5)

if __name__ == '__main__':
    unittest.main()


This test suite covers a variety of scenarios, including:

* Small and large numbers
* Numbers with common divisors
* Numbers with no common divisors
* Negative numbers
* Positive and negative numbers
* Zero numbers
* Numbers with one zero
* Numbers with one negative number

Each test case checks the output of the `greatest_common_divisor` function against the expected result using the `assertEqual` method.