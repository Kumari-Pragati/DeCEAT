system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_75_code import is_multiply_prime
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less than 100. 
    Example:
        is_multiply_prime(30) == True
        30 = 2 * 3 * 5
    """

    def is_prime(n):
        for j in range(2, n):
            if n % j == 0:
                return False
        return True

    for i in range(2, 101):
        if not is_prime(i):
            continue
        for j in range(2, 101):
            if not is_prime(j):
                continue
            for k in range(2, 101):
                if not is_prime(k):
                    continue
                if i * j * k == a:
                    return True
    return False


assistant

import unittest

# Importing the function to be tested
from HumanEval_75_code import is_multiply_prime

class TestIsMultiplyPrime(unittest.TestCase):

    def test_is_multiply_prime(self):
        # Test cases covering various scenarios
        self.assertTrue(is_multiply_prime(30))  # 2 * 3 * 5
        self.assertFalse(is_multiply_prime(49))  # Not a product of three primes
        self.assertTrue(is_multiply_prime(60))   # 2 * 3 * 5 * 2
        self.assertFalse(is_multiply_prime(84))  # 2 * 3 * 7 * 2
        self.assertTrue(is_multiply_prime(91))   # 7 * 13
        self.assertFalse(is_multiply_prime(100)) # Not a product of three primes

if __name__ == '__main__':
    unittest.main()


This script imports the `is_multiply_prime` function and defines a class `TestIsMultiplyPrime` within a test case module named `unittest`. It includes several test methods (`test_is_multiply_prime`) to cover different scenarios as specified in the problem description. The `unittest.main()` call at the end makes the tests executable when run directly.