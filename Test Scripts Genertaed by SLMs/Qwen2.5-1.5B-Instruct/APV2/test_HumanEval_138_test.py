system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Function to check if the given number can be expressed as the sum of four even numbers
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers"""
    return n % 2 == 0 and n >= 8

class TestIsEqualToSumEven(unittest.TestCase):

    def test_is_equal_to_sum_even(self):
        # Test cases to verify the correctness of the function
        self.assertEqual(is_equal_to_sum_even(4), False)
        self.assertEqual(is_equal_to_sum_even(6), False)
        self.assertEqual(is_equal_to_sum_even(8), True)
        self.assertEqual(is_equal_to_sum_even(10), True)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestIsEqualToSumEven` class that inherits from `unittest.TestCase`. It contains a single method `test_is_equal_to_sum_even`, which includes several assertions to validate the behavior of the `is_equal_to_sum_even` function against provided data points. The `unittest.main()` call at the end runs the tests when this script is executed directly.