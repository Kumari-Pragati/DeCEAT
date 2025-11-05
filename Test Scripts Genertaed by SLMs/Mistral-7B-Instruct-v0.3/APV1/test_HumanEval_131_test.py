You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_131_code import digits

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    product = 1
    odd_count = 0
    for digit in str(n):
        int_digit = int(digit)
        if int_digit % 2 == 1:
            product = product * int_digit
            odd_count += 1
    if odd_count == 0:
        return 0
    else:
        return product

 Here is a comprehensive unittest test suite for the given Python function `digits(n)`. The test suite includes a variety of test cases to ensure the function works correctly for different inputs.


import unittest
from HumanEval_131_code import digits

class TestDigitsFunction(unittest.TestCase):

    def test_digits_1(self):
        self.assertEqual(digits(1), 1)

    def test_digits_4(self):
        self.assertEqual(digits(4), 0)

    def test_digits_235(self):
        self.assertEqual(digits(235), 15)

    def test_digits_12345(self):
        self.assertEqual(digits(12345), 15)

    def test_digits_1000005(self):
        self.assertEqual(digits(1000005), 5)

    def test_digits_12300045(self):
        self.assertEqual(digits(12300045), 45)

    def test_digits_123000045(self):
        self.assertEqual(digits(123000045), 0)

    def test_digits_0(self):
        self.assertEqual(digits(0), 0)

    def test_digits_negative_number(self):
        self.assertEqual(digits(-123), 0)

    def test_digits_large_number(self):
        large_number = 12345678901234567890
        self.assertEqual(digits(large_number), 7)

if __name__ == '__main__':
    unittest.main()


This test suite includes test cases for positive integers, negative integers, zero, and large numbers. It also tests the edge case where all digits are even.