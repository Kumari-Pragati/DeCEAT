user

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

    return power == xassistant

Here is a comprehensive unittest test suite for the given Python function `is_simple_power`:


import unittest
from HumanEval_76_code import is_simple_power

class TestIsSimplePower(unittest.TestCase):

    def test_is_simple_power(self):
        # Test cases where x is a simple power of n
        self.assertTrue(is_simple_power(1, 4))  # 1 is a simple power of 4
        self.assertTrue(is_simple_power(2, 2))  # 2 is a simple power of 2
        self.assertTrue(is_simple_power(8, 2))  # 8 is a simple power of 2
        self.assertTrue(is_simple_power(1, 1))  # 1 is a simple power of 1

        # Test cases where x is not a simple power of n
        self.assertFalse(is_simple_power(3, 2))  # 3 is not a simple power of 2
        self.assertFalse(is_simple_power(3, 1))  # 3 is not a simple power of 1
        self.assertFalse(is_simple_power(5, 3))  # 5 is not a simple power of 3
        self.assertFalse(is_simple_power(4, 3))  # 4 is not a simple power of 3

        # Test cases where n is 1
        self.assertTrue(is_simple_power(1, 1))  # 1 is a simple power of 1
        self.assertFalse(is_simple_power(2, 1))  # 2 is not a simple power of 1

        # Test cases where x is 0
        self.assertFalse(is_simple_power(0, 1))  # 0 is not a simple power of 1
        self.assertFalse(is_simple_power(0, 2))  # 0 is not a simple power of 2

        # Test cases where n is 0
        self.assertFalse(is_simple_power(1, 0))  # 1 is not a simple power of 0
        self.assertFalse(is_simple_power(2, 0))  # 2 is not a simple power of 0

if __name__ == '__main__':
    unittest.main()


This test suite covers various test cases, including:

* Test cases where x is a simple power of n
* Test cases where x is not a simple power of n
* Test cases where n is 1
* Test cases where x is 0
* Test cases where n is 0

The test suite uses the `assertTrue` and `assertFalse` methods to verify that the `is_simple_power` function returns the expected results for each test case.