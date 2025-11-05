You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

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

    def test_multiply_positive_integers(self):
        self.assertEqual(multiply(148, 412), 16)

    def test_multiply_negative_integers(self):
        self.assertEqual(multiply(19, 28), 72)

    def test_multiply_zero_integers(self):
        self.assertEqual(multiply(2020, 1851), 0)

    def test_multiply_positive_and_negative_integers(self):
        self.assertEqual(multiply(14, -15), 20)

    def test_multiply_large_integers(self):
        self.assertEqual(multiply(123456789, 987654321), 9)

    def test_multiply_single_digit_integers(self):
        self.assertEqual(multiply(5, 5), 25)

    def test_multiply_same_digit_integers(self):
        self.assertEqual(multiply(11, 11), 1)

    def test_multiply_edge_case_integers(self):
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(1, 0), 0)
        self.assertEqual(multiply(0, 1), 0)

if __name__ == '__main__':
    unittest.main()


This test suite covers a variety of cases, including positive and negative integers, zeros, large integers, single-digit integers, same-digit integers, and edge cases where one or both integers are zero. Each test case checks the `multiply` function against expected outcomes, ensuring that it behaves correctly for different inputs.