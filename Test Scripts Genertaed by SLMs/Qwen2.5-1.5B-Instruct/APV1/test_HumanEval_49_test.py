system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_49_code import modp
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def modp(n: int, p: int):
    """Return 2^n modulo p (be aware of numerics).
    >>> modp(3, 5)
    3
    >>> modp(1101, 101)
    2
    >>> modp(0, 101)
    1
    >>> modp(3, 11)
    8
    >>> modp(100, 101)
    1
    """
    ret = 1
    for i in range(n):
        ret = (2 * ret) % p
    return ret


assistant

import unittest

# Importing the function from the module
from HumanEval_49_code import modp

class TestModp(unittest.TestCase):

    def test_modp(self):
        # Test cases provided in the docstring
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)

    def test_edge_cases(self):
        # Edge case tests
        self.assertEqual(modp(0, 7), 1)
        self.assertEqual(modp(1, 7), 1)
        self.assertEqual(modp(6, 7), 6)
        self.assertEqual(modp(7, 7), 1)
        self.assertEqual(modp(10, 7), 2)

    def test_large_numbers(self):
        # Large number tests
        self.assertEqual(modp(10**10, 10**10 + 1), 1)
        self.assertEqual(modp(10**100, 10**100 + 1), 1)

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestModp` class that inherits from `unittest.TestCase`. It contains several test methods to verify the correctness of the `modp` function using both positive and edge cases as well as large numbers. The `unittest.main()` call at the end runs all the defined test methods when this script is executed directly.