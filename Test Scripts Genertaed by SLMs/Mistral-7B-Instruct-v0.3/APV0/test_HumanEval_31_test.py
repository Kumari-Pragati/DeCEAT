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
    return True

 Here is a simple unittest test script for the `is_prime` function. It covers the edge cases and a range of numbers to ensure the function works as expected.


import unittest
from HumanEval_31_code import is_prime

class TestIsPrime(unittest.TestCase):

    def test_is_prime_positive_numbers(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(17))
        self.assertTrue(is_prime(19))
        self.assertTrue(is_prime(23))
        self.assertTrue(is_prime(29))
        self.assertTrue(is_prime(31))
        self.assertTrue(is_prime(101))
        self.assertTrue(is_prime(13441))
        self.assertTrue(is_prime(61))

    def test_is_not_prime_numbers(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(14))
        self.assertFalse(is_prime(15))
        self.assertFalse(is_prime(16))
        self.assertFalse(is_prime(18))
        self.assertFalse(is_prime(20))
        self.assertFalse(is_prime(22))
        self.assertFalse(is_prime(24))
        self.assertFalse(is_prime(25))
        self.assertFalse(is_prime(26))
        self.assertFalse(is_prime(30))
        self.assertFalse(is_prime(32))
        self.assertFalse(is_prime(33))
        self.assertFalse(is_prime(34))
        self.assertFalse(is_prime(35))
        self.assertFalse(is_prime(36))
        self.assertFalse(is_prime(37))
        self.assertFalse(is_prime(38))
        self.assertFalse(is_prime(39))
        self.assertFalse(is_prime(40))
        self.assertFalse(is_prime(41))
        self.assertFalse(is_prime(42))
        self.assertFalse(is_prime(43))
        self.assertFalse(is_prime(44))
        self.assertFalse(is_prime(45))
        self.assertFalse(is_prime(46))
        self.assertFalse(is_prime(47))
        self.assertFalse(is_prime(48))
        self.assertFalse(is_prime(49))
        self.assertFalse(is_prime(50))

if __name__ == '__main__':
    unittest.main()


This test script includes two test cases: one for positive numbers that are prime and another for positive numbers that are not prime. It covers a wide range of numbers to ensure the function works as expected.