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
    return retassistant

Here is the unittest test script for the `modp` function:

import unittest
from HumanEval_49_code import modp

class TestModp(unittest.TestCase):
    def test_modp(self):
        # Test cases from the docstring
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)

        # Additional test cases
        self.assertEqual(modp(1, 2), 1)
        self.assertEqual(modp(2, 3), 2)
        self.assertEqual(modp(4, 5), 4)
        self.assertEqual(modp(5, 7), 4)
        self.assertEqual(modp(10, 11), 1)

        # Edge cases
        self.assertEqual(modp(-1, 2), 1)
        self.assertEqual(modp(0, 2), 1)
        self.assertEqual(modp(1, 0), 0)  # Note: p=0 is not a valid input

if __name__ == '__main__':
    unittest.main()

This script defines a `TestModp` class that contains several test methods. Each test method tests a specific input to the `modp` function using the `assertEqual` method. The test cases cover a variety of inputs, including positive and negative integers, zero, and edge cases where `p` is zero.

To run the tests, save this script to a file (e.g., `test_modp.py`) and execute it using the `python` command:

$ python test_modp.py

This will run the tests and report any failures or errors.