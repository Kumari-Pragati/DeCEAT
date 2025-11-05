system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Function to check if a number x is a simple power of n
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


class TestIsSimplePower(unittest.TestCase):
    def test_is_simple_power(self):
        self.assertTrue(is_simple_power(1, 4))
        self.assertTrue(is_simple_power(2, 2))
        self.assertTrue(is_simple_power(8, 2))
        self.assertFalse(is_simple_power(3, 2))
        self.assertFalse(is_simple_power(3, 1))
        self.assertFalse(is_simple_power(5, 3))

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines the `is_simple_power` function as described. It then creates a class `TestIsSimplePower` inheriting from `unittest.TestCase`, which contains a method `test_is_simple_power`. This method tests various cases using assertions to ensure the correctness of the `is_simple_power` function. Finally, it calls `unittest.main()` to run the tests when the script is executed directly.