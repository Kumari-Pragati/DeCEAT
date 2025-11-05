Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

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

 import unittest
from HumanEval_138_code import is_equal_to_sum_even

class TestIsEqualToSumEven(unittest.TestCase):

    def test_even_numbers_sum_less_than_8(self):
        self.assertFalse(is_equal_to_sum_even(4))
        self.assertFalse(is_equal_to_sum_even(6))

    def test_even_numbers_sum_equal_8(self):
        self.assertTrue(is_equal_to_sum_even(8))

    def test_even_numbers_sum_greater_than_8(self):
        self.assertTrue(is_equal_to_sum_even(10))
        self.assertTrue(is_equal_to_sum_even(12))
        self.assertTrue(is_equal_to_sum_even(14))

    def test_odd_numbers(self):
        self.assertFalse(is_equal_to_sum_even(7))
        self.assertFalse(is_equal_to_sum_even(9))
        self.assertFalse(is_equal_to_sum_even(11))

    def test_zero(self):
        self.assertFalse(is_equal_to_sum_even(0))

    def test_negative_numbers(self):
        self.assertFalse(is_equal_to_sum_even(-1))
        self.assertFalse(is_equal_to_sum_even(-2))
        self.assertFalse(is_equal_to_sum_even(-4))

if __name__ == '__main__':
    unittest.main()