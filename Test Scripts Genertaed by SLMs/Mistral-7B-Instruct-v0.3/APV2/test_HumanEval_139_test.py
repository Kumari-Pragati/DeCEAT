You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_139_code import special_factorial
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    fact_i = 1
    special_fact = 1
    for i in range(1, n + 1):
        fact_i *= i
        special_fact *= fact_i
    return special_fact

 Here is the complete unittest test suite for the `special_factorial` function:


import unittest
from HumanEval_139_code import special_factorial

class TestSpecialFactorial(unittest.TestCase):

    def test_special_factorial_positive(self):
        """Test special_factorial with positive integers"""
        self.assertEqual(special_factorial(1), 1)
        self.assertEqual(special_factorial(2), 2)
        self.assertEqual(special_factorial(3), 6)
        self.assertEqual(special_factorial(4), 288)
        self.assertEqual(special_factorial(5), 15120)
        self.assertEqual(special_factorial(6), 933160)

    def test_special_factorial_zero(self):
        """Test special_factorial with zero"""
        self.assertRaises(ValueError, special_factorial, 0)

    def test_special_factorial_negative(self):
        """Test special_factorial with negative integers"""
        self.assertRaises(ValueError, special_factorial, -1)
        self.assertRaises(ValueError, special_factorial, -2)

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_special_factorial_positive` tests the function with positive integers.
2. `test_special_factorial_zero` tests the function with zero.
3. `test_special_factorial_negative` tests the function with negative integers.

The test suite uses the `unittest.TestCase` class to define test methods and the `unittest.main()` function to run the tests. The `assertEqual` and `assertRaises` methods are used to verify the expected behavior of the `special_factorial` function.