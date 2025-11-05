You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_83_code import starts_one_ends
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n == 1:
        return 1
    return 18 * (10 ** (n - 2))


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_83_code import starts_one_ends

class TestStartsOneEnds(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(starts_one_ends(1), 1)

    def test_double_digit(self):
        self.assertEqual(starts_one_ends(2), 18)

    def test_multi_digit(self):
        self.assertEqual(starts_one_ends(3), 180)

    def test_zero_digit(self):
        with self.assertRaises(TypeError):
            starts_one_ends(0)

    def test_negative_digit(self):
        with self.assertRaises(ValueError):
            starts_one_ends(-1)

    def test_large_digit(self):
        self.assertEqual(starts_one_ends(10), 18000000000)

if __name__ == '__main__':
    unittest.main()


This script tests the function with different inputs, including single-digit, double-digit, and multi-digit numbers. It also tests the function with zero and negative numbers, and with a large number. The script uses the unittest framework's assertEqual and assertRaises methods to check that the function's output matches the expected output and that it raises an error when given invalid input.