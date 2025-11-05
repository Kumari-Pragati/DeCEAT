You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is the complete unittest test suite for the `digits` function:


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

    def test_digits_0(self):
        self.assertEqual(digits(0), 0)

    def test_digits_negative_number(self):
        self.assertEqual(digits(-123), 0)

    def test_digits_large_number(self):
        self.assertEqual(digits(123456789), 13579)

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases for different inputs, including positive numbers, negative numbers, and zero. It also tests the edge case where all digits are even and the product should be zero. The test suite uses the `unittest.TestCase.assertEqual` method to verify that the expected output matches the actual output of the `digits` function.