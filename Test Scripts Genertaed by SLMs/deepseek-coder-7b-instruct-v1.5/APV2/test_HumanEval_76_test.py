You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
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


### Response:
Here's a unittest test suite for the `is_simple_power` function:


import unittest
from HumanEval_76_code import is_simple_power

class TestIsSimplePower(unittest.TestCase):

    def test_simple_powers(self):
        # Test cases where x is a simple power of n
        self.assertTrue(is_simple_power(1, 4))
        self.assertTrue(is_simple_power(2, 2))
        self.assertTrue(is_simple_power(8, 2))

    def test_not_simple_powers(self):
        # Test cases where x is not a simple power of n
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(3, 1))
        self.assertFalse(is_simple_power(5, 3))

    def test_edge_cases(self):
        # Test edge cases
        self.assertTrue(is_simple_power(1, 1))
        self.assertFalse(is_simple_power(0, 2))
        self.assertFalse(is_simple_power(-1, 2))

if __name__ == '__main__':
    unittest.main()


This suite includes tests for simple powers, cases where `x` is not a simple power of `n`, and edge cases where `x` is 1 or 0. It uses the `assertTrue` and `assertFalse` methods to check if the function returns the correct boolean value for each test case.