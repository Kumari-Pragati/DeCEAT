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

 import unittest
from HumanEval_138_code import is_equal_to_sum_even

class TestIsEqualToSumEven(unittest.TestCase):

    def test_even_numbers(self):
        self.assertFalse(is_equal_to_sum_even(4))
        self.assertFalse(is_equal_to_sum_even(6))
        self.assertTrue(is_equal_to_sum_even(8))
        self.assertTrue(is_equal_to_sum_even(10))
        self.assertTrue(is_equal_to_sum_even(12))
        self.assertFalse(is_equal_to_sum_even(11))
        self.assertFalse(is_equal_to_sum_even(7))
        self.assertFalse(is_equal_to_sum_even(1))
        self.assertFalse(is_equal_to_sum_even(0))

    def test_edge_cases(self):
        self.assertFalse(is_equal_to_sum_even(-1))
        self.assertFalse(is_equal_to_sum_even(0))
        self.assertFalse(is_equal_to_sum_even(1))

    def test_large_numbers(self):
        self.assertTrue(is_equal_to_sum_even(80))
        self.assertTrue(is_equal_to_sum_even(100))
        self.assertTrue(is_equal_to_sum_even(120))
        self.assertTrue(is_equal_to_sum_even(140))

if __name__ == '__main__':
    unittest.main()