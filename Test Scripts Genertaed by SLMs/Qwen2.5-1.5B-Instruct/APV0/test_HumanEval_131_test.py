system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
        return product


assistant

import unittest

# Function to be tested
from HumanEval_131_code import digits

class TestDigits(unittest.TestCase):

    def test_digits(self):
        self.assertEqual(digits(1), 1)
        self.assertEqual(digits(4), 0)
        self.assertEqual(digits(235), 15)

    def test_all_even(self):
        self.assertEqual(digits(222), 0)

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` module, defines the function `digits`, and includes two test cases within the class `TestDigits`. The first test case checks that the function returns the correct result for different inputs. The second test case ensures that when all digits are even, the function correctly returns 0. Finally, it runs the tests using `unittest.main()`.