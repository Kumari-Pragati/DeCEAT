You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code. Write a complete unittest test suite for the following Python function. 
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_76_code import is_simple_power
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_simple_power(x, n):
    """Your task is to write a function that returns true if a number x is a simple
    power of n and false in other cases.
    x is a simple power of n if n**int = x
    For example:
        is_simple_power(1, 4) => True
        is_simple_power(2, 2) => True
        is_simple_power(8, 2) => True
        is_simple_power(3, 2) => False
        is_simple_power(3, 1) => False
        is_simple_power(5, 3) => False
    """

    if n == 1:
        return x == 1

    power = 1
    while power < x:
        power *= n

    return power == x

 
import unittest
from HumanEval_76_code import is_simple_power

class TestIsSimplePower(unittest.TestCase):

    def test_is_simple_power_true(self):
        self.assertTrue(is_simple_power(1, 4))
        self.assertTrue(is_simple_power(2, 2))
        self.assertTrue(is_simple_power(8, 2))

    def test_is_simple_power_false(self):
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(3, 1))
        self.assertFalse(is_simple_power(5, 3))
        self.assertFalse(is_simple_power(10, 2))
        self.assertFalse(is_simple_power(16, 3))
        self.assertFalse(is_simple_power(7, 4))

    def test_is_simple_power_edge_cases(self):
        self.assertTrue(is_simple_power(1, 1))
        self.assertTrue(is_simple_power(1, 0))
        self.assertFalse(is_simple_power(0, 1))
        self.assertFalse(is_simple_power(0, 0))

    def test_is_simple_power_negative_numbers(self):
        self.assertFalse(is_simple_power(-1, 2))
        self.assertFalse(is_simple_power(-2, 2))
        self.assertFalse(is_simple_power(-8, 2))

    def test_is_simple_power_zero(self):
        self.assertFalse(is_simple_power(0, 2))
        self.assertFalse(is_simple_power(0, 0))

    def test_is_simple_power_non_integer_exponents(self):
        self.assertFalse(is_simple_power(8, 2.5))
        self.assertFalse(is_simple_power(16, 1.5))

if __name__ == '__main__':
    unittest.main()


This test suite covers a variety of cases, including positive numbers, negative numbers, zero, and non-integer exponents. It ensures that the `is_simple_power` function behaves as expected according to the provided specifications.