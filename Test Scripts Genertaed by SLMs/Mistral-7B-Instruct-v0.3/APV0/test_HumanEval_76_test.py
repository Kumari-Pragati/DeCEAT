Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `is_simple_power` function:


import unittest
from HumanEval_76_code import is_simple_power

class TestIsSimplePower(unittest.TestCase):
    def test_simple_power(self):
        self.assertTrue(is_simple_power(1, 1))
        self.assertTrue(is_simple_power(4, 2))
        self.assertTrue(is_simple_power(8, 3))
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(1, 2))
        self.assertFalse(is_simple_power(5, 3))

    def test_negative_base(self):
        self.assertFalse(is_simple_power(-1, 2))
        self.assertFalse(is_simple_power(-2, 2))

    def test_zero_base(self):
        self.assertFalse(is_simple_power(0, 2))

    def test_zero_exponent(self):
        self.assertTrue(is_simple_power(0, 0))
        self.assertFalse(is_simple_power(1, 0))

    def test_large_numbers(self):
        self.assertTrue(is_simple_power(1024, 2))
        self.assertTrue(is_simple_power(16807, 3))
        self.assertFalse(is_simple_power(1025, 2))
        self.assertFalse(is_simple_power(16808, 3))

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases to cover different scenarios, such as simple powers, negative bases, zero base, zero exponent, and large numbers. It also includes a test for the edge case when `x` is equal to 1, which the original function handles differently.