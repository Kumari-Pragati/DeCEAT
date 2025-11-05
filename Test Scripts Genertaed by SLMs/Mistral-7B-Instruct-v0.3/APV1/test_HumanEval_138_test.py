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
    return n % 2 == 0 and n >= 8

 Here is a comprehensive unittest test suite for the given Python function `is_equal_to_sum_even(n)`.


import unittest
from HumanEval_138_code import is_equal_to_sum_even

class TestIsEqualToSumEven(unittest.TestCase):

    def test_negative_numbers(self):
        self.assertFalse(is_equal_to_sum_even(-1))
        self.assertFalse(is_equal_to_sum_even(-2))
        self.assertFalse(is_equal_to_sum_even(-4))
        self.assertFalse(is_equal_to_sum_even(-8))

    def test_even_numbers_less_than_8(self):
        self.assertFalse(is_equal_to_sum_even(0))
        self.assertFalse(is_equal_to_sum_even(2))
        self.assertFalse(is_equal_to_sum_even(4))
        self.assertFalse(is_equal_to_sum_even(6))
        self.assertFalse(is_equal_to_sum_even(8))

    def test_even_numbers_greater_than_8_but_not_divisible_by_4(self):
        self.assertFalse(is_equal_to_sum_even(10))
        self.assertFalse(is_equal_to_sum_even(12))
        self.assertFalse(is_equal_to_sum_even(14))
        self.assertFalse(is_equal_to_sum_even(16))
        self.assertFalse(is_equal_to_sum_even(18))

    def test_even_numbers_divisible_by_4_but_not_4(self):
        self.assertFalse(is_equal_to_sum_even(20))
        self.assertFalse(is_equal_to_sum_even(24))
        self.assertFalse(is_equal_to_sum_even(28))
        self.assertFalse(is_equal_to_sum_even(32))
        self.assertFalse(is_equal_to_sum_even(36))

    def test_even_numbers_equal_to_4*k(k>=2)(self):
        for k in range(2, 10):
            n = 4 * k
            self.assertTrue(is_equal_to_sum_even(n))

    def test_even_numbers_greater_than_4*k(k>=2)_but_not_4*k+2(self):
        for k in range(2, 10):
            n = 4 * k + 2
            self.assertFalse(is_equal_to_sum_even(n))

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases for negative numbers, even numbers less than 8, even numbers greater than 8 but not divisible by 4, even numbers divisible by 4 but not 4, and even numbers equal to 4*k (k>=2) and greater than 4*k but not 4*k + 2.