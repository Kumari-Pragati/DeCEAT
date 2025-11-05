You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return True

 Here is a complete unittest test suite for the `is_prime` function:


import unittest
from HumanEval_31_code import is_prime

class TestIsPrime(unittest.TestCase):

    def test_is_prime_positive_numbers(self):
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(41))
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(13441))
        self.assertTrue(is_prime(61))

    def test_is_not_prime_positive_numbers(self):
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(20))
        self.assertFalse(is_prime(36))
        self.assertFalse(is_prime(40))
        self.assertFalse(is_prime(50))
        self.assertFalse(is_prime(60))

    def test_is_not_prime_zero_and_negative_numbers(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-3))
        self.assertFalse(is_prime(-4))
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-6))

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_is_prime_positive_numbers` checks that the function correctly identifies prime numbers.
2. `test_is_not_prime_positive_numbers` checks that the function correctly identifies non-prime numbers.
3. `test_is_not_prime_zero_and_negative_numbers` checks that the function correctly identifies that zero and negative numbers are not prime.