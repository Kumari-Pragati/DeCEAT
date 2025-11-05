You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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

 Here is a complete unittest test suite for the `is_equal_to_sum_even` function:


import unittest
from HumanEval_138_code import is_equal_to_sum_even

class TestIsEqualToSumEven(unittest.TestCase):

    def test_negative_numbers(self):
        self.assertFalse(is_equal_to_sum_even(-1))
        self.assertFalse(is_equal_to_sum_even(-2))
        self.assertFalse(is_equal_to_sum_even(-4))

    def test_even_numbers_less_than_8(self):
        self.assertFalse(is_equal_to_sum_even(2))
        self.assertFalse(is_equal_to_sum_even(4))
        self.assertFalse(is_equal_to_sum_even(6))
        self.assertFalse(is_equal_to_sum_even(8))

    def test_even_numbers_greater_than_8(self):
        self.assertTrue(is_equal_to_sum_even(10))
        self.assertTrue(is_equal_to_sum_even(12))
        self.assertTrue(is_equal_to_sum_even(14))
        self.assertTrue(is_equal_to_sum_even(16))

    def test_odd_numbers(self):
        self.assertFalse(is_equal_to_sum_even(1))
        self.assertFalse(is_equal_to_sum_even(3))
        self.assertFalse(is_equal_to_sum_even(5))
        self.assertFalse(is_equal_to_sum_even(7))

if __name__ == '__main__':
    unittest.main()


This test suite includes four test cases:

1. `test_negative_numbers` checks that the function returns `False` for negative numbers.
2. `test_even_numbers_less_than_8` checks that the function returns `False` for even numbers less than 8.
3. `test_even_numbers_greater_than_8` checks that the function returns `True` for even numbers greater than or equal to 8.
4. `test_odd_numbers` checks that the function returns `False` for odd numbers.

Each test case includes multiple assertions to cover a range of possible inputs.