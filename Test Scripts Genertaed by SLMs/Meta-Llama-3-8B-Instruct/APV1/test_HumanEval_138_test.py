user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_138_code import is_equal_to_sum_even
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return n % 2 == 0 and n >= 8assistant

Here is the comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_138_code import is_equal_to_sum_even

class TestIsEqualToSumEven(unittest.TestCase):

    def test_is_equal_to_sum_even_positive_numbers(self):
        self.assertTrue(is_equal_to_sum_even(8))
        self.assertTrue(is_equal_to_sum_even(10))
        self.assertTrue(is_equal_to_sum_even(12))
        self.assertTrue(is_equal_to_sum_even(14))

    def test_is_equal_to_sum_even_negative_numbers(self):
        self.assertFalse(is_equal_to_sum_even(-8))
        self.assertFalse(is_equal_to_sum_even(-10))
        self.assertFalse(is_equal_to_sum_even(-12))
        self.assertFalse(is_equal_to_sum_even(-14))

    def test_is_equal_to_sum_even_zero(self):
        self.assertFalse(is_equal_to_sum_even(0))

    def test_is_equal_to_sum_even_non_integer(self):
        self.assertFalse(is_equal_to_sum_even(3.5))

    def test_is_equal_to_sum_even_numbers_greater_than_8(self):
        self.assertTrue(is_equal_to_sum_even(16))
        self.assertTrue(is_equal_to_sum_even(18))
        self.assertTrue(is_equal_to_sum_even(20))

    def test_is_equal_to_sum_even_numbers_less_than_8(self):
        self.assertFalse(is_equal_to_sum_even(4))
        self.assertFalse(is_equal_to_sum_even(6))
        self.assertFalse(is_equal_to_sum_even(7))

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases to cover different scenarios, such as positive and negative numbers, zero, non-integer numbers, numbers greater than 8, and numbers less than 8. The test cases are designed to ensure that the function behaves correctly in all these scenarios.