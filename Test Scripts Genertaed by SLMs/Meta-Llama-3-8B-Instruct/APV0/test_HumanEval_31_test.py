user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_31_code import is_prime
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    if n < 2:
        return False
    for k in range(2, n - 1):
        if n % k == 0:
            return False
    return Trueassistant

Here is the unittest test script for the `is_prime` function:

import unittest
from HumanEval_31_code import is_prime

class TestIsPrime(unittest.TestCase):
    def test_small_primes(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))

    def test_small_non_primes(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))

    def test_large_primes(self):
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13441))
        self.assertTrue(is_prime(61))

    def test_edge_cases(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(2))  # should return False for 2, not True
        self.assertFalse(is_prime(0))  # 0 is not a prime number
        self.assertFalse(is_prime(-1))  # -1 is not a prime number

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_prime("hello")
        with self.assertRaises(TypeError):
            is_prime(None)

if __name__ == '__main__':
    unittest.main()

This test script covers the following cases:

1. Small prime numbers (2, 3, 5, 7)
2. Small non-prime numbers (4, 6, 8, 9)
3. Large prime numbers (101, 11, 13441, 61)
4. Edge cases (1, 2, 0, -1)
5. Invalid input (strings, None)

The `unittest` framework provides a convenient way to write and run tests. The `TestIsPrime` class contains five test methods, each of which tests a specific aspect of the `is_prime` function. The `assert` statements are used to verify that the function behaves correctly in each case.

To run the tests, simply execute the script. The `unittest` framework will automatically discover and run the tests.