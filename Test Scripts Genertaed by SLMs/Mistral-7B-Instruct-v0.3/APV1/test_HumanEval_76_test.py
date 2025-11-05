You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the `is_simple_power` function:


import unittest
from HumanEval_76_code import is_simple_power

class TestIsSimplePower(unittest.TestCase):
    def test_simple_power(self):
        self.assertTrue(is_simple_power(1, 1))
        self.assertTrue(is_simple_power(4, 2))
        self.assertTrue(is_simple_power(8, 3))

    def test_non_simple_power(self):
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(2, 1))
        self.assertFalse(is_simple_power(5, 3))
        self.assertFalse(is_simple_power(0, 2))
        self.assertFalse(is_simple_power(10, 3))

    def test_edge_cases(self):
        self.assertFalse(is_simple_power(0, 0))
        self.assertFalse(is_simple_power(1, 0))
        self.assertFalse(is_simple_power(-1, 2))
        self.assertFalse(is_simple_power(1, -1))

if __name__ == '__main__':
    unittest.main()


This test suite includes three test methods:

1. `test_simple_power`: Tests cases where the input number is a simple power of the base number.
2. `test_non_simple_power`: Tests cases where the input number is not a simple power of the base number.
3. `test_edge_cases`: Tests edge cases that may cause issues, such as inputting 0 or negative numbers.

The test suite uses the `unittest.TestCase` class to define test methods, and the `unittest.main()` function to run the tests.