user

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
        return productassistant

Here is a unittest test script for the given Python function:

Python
import unittest
from HumanEval_131_code import digits

class TestDigitsFunction(unittest.TestCase):

    def test_digits(self):
        self.assertEqual(digits(1), 1)
        self.assertEqual(digits(4), 0)
        self.assertEqual(digits(235), 15)
        self.assertEqual(digits(246), 0)
        self.assertEqual(digits(13579), 945)
        self.assertEqual(digits(123456), 0)
        self.assertEqual(digits(123456789), 315)

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to ensure the function is working correctly. The test cases cover a variety of inputs, including single-digit numbers, multi-digit numbers with and without odd digits, and numbers with no odd digits. The `assertEqual` method is used to compare the output of the function with the expected output. If the function is working correctly, all of these assertions should pass.