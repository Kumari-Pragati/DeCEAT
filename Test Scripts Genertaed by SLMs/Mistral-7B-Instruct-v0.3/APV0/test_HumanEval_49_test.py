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

 Here is a unittest test script for the provided `modp` function. The test cases cover the edge cases and various inputs mentioned in the function's documentation string.


import unittest
from HumanEval_49_code import modp

class TestModP(unittest.TestCase):

    def test_modp(self):
        self.assertEqual(modp(3, 5), 3)
        self.assertEqual(modp(1101, 101), 2)
        self.assertEqual(modp(0, 101), 1)
        self.assertEqual(modp(3, 11), 8)
        self.assertEqual(modp(100, 101), 1)
        self.assertEqual(modp(-3, 5), 3)  # Testing negative input
        self.assertEqual(modp(1000000000000000000, 10), 1)  # Testing large inputs
        self.assertEqual(modp(0, 0), ValueError)  # Testing zero divisor
        self.assertEqual(modp(1, 0), ValueError)  # Testing zero divisor

if __name__ == '__main__':
    unittest.main()


This test script includes a `TestModP` class that defines a test case for the `modp` function. The `test_modp` method contains various test cases to ensure the function behaves as expected. The test cases cover edge cases, negative inputs, large inputs, and zero divisors. The script will run the tests when executed directly.