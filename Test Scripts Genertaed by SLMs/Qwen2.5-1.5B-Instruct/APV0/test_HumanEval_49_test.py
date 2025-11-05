system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

# Importing the function to be tested
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
        self.assertEqual(modp(-1, 7), 6)
        self.assertEqual(modp(7, -1), 6)
        self.assertEqual(modp(0, 0), 1)
        self.assertEqual(modp(1, 1), 1)
        self.assertEqual(modp(10**10, 10**10 + 1), 10**10)

if __name__ == '__main__':
    unittest.main()


This script imports the `modp` function and defines a class `TestModp` that inherits from `unittest.TestCase`. It contains two methods: `test_modp`, which tests the main functionality of `modp`, and `test_edge_cases`, which includes additional edge cases to ensure robustness. The `unittest.main()` call at the end makes the script executable when run as a standalone program.