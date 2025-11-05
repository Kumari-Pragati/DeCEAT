Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

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

 import unittest
from HumanEval_131_code import digits

class TestDigitsFunction(unittest.TestCase):

    def test_single_odd_digit(self):
        self.assertEqual(digits(1), 1)

    def test_single_even_digit(self):
        self.assertEqual(digits(4), 0)

    def test_multiple_odd_digits(self):
        self.assertEqual(digits(235), 15)

    def test_all_even_digits(self):
        self.assertEqual(digits(2468), 0)

    def test_zero_input(self):
        self.assertEqual(digits(0), 0)

    def test_negative_input(self):
        self.assertEqual(digits(-123), 3)

    def test_single_digit_number(self):
        self.assertEqual(digits(7), 7)

    def test_multiple_digit_number(self):
        self.assertEqual(digits(123456), 90)

    def test_number_with_no_odd_digits(self):
        self.assertEqual(digits(222222), 0)

    def test_number_with_all_odd_digits(self):
        self.assertEqual(digits(13579), 9405)

if __name__ == '__main__':
    unittest.main()