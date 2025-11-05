user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

    return abs(a % 10) * abs(b % 10)assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_97_code import multiply

class TestMultiply(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)
        self.assertEqual(multiply(2020, 1851), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(14, -15), 20)
        self.assertEqual(multiply(-14, 15), 20)
        self.assertEqual(multiply(-14, -15), 20)

    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(10, 0), 0)

    def test_multiply_non_integer(self):
        with self.assertRaises(TypeError):
            multiply(14.5, 15)
        with self.assertRaises(TypeError):
            multiply(14, 15.5)

    def test_multiply_invalid_input(self):
        with self.assertRaises(TypeError):
            multiply("14", 15)
        with self.assertRaises(TypeError):
            multiply(14, "15")

if __name__ == '__main__':
    unittest.main()


This test suite covers various test cases, including:

- Test cases for positive numbers
- Test cases for negative numbers
- Test cases for zero
- Test cases for non-integer inputs
- Test cases for invalid inputs (non-integer and non-numeric inputs)

Each test case checks the output of the `multiply` function against the expected output. The `assertEqual` method is used to check if the output is as expected, and the `assertRaises` method is used to check if the function raises the expected error.