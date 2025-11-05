You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_59_code import largest_prime_factor
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(k):
        if k < 2:
            return False
        for i in range(2, k - 1):
            if k % i == 0:
                return False
        return True

    largest = 1
    for j in range(2, n + 1):
        if n % j == 0 and is_prime(j):
            largest = max(largest, j)
    return largest

 import unittest
from HumanEval_59_code import largest_prime_factor

class TestLargestPrimeFactor(unittest.TestCase):

    def test_largest_prime_factor_13195(self):
        self.assertEqual(largest_prime_factor(13195), 29)

    def test_largest_prime_factor_2048(self):
        self.assertEqual(largest_prime_factor(2048), 2)

    def test_largest_prime_factor_100(self):
        self.assertEqual(largest_prime_factor(100), 5)

    def test_largest_prime_factor_1(self):
        with self.assertRaises(ValueError):
            largest_prime_factor(1)

    def test_largest_prime_factor_prime_number(self):
        self.assertEqual(largest_prime_factor(2), 2)

    def test_largest_prime_factor_negative_number(self):
        with self.assertRaises(ValueError):
            largest_prime_factor(-1)

if __name__ == '__main__':
    unittest.main()