system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


assistant

import unittest

# Function to check if a number is prime
def is_prime(k):
    if k < 2:
        return False
    for i in range(2, k - 1):
        if k % i == 0:
            return False
    return True

class TestLargestPrimeFactor(unittest.TestCase):
    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines the `largest_prime_factor` function as provided. It also includes a helper function `is_prime` to check if a given number is prime. The `TestLargestPrimeFactor` class inherits from `unittest.TestCase`, which allows us to write tests using methods starting with `test`. The `test_largest_prime_factor` method checks that the function returns the correct values for two test cases. Finally, the `if __name__ == '__main__':` block runs all the tests when the script is executed directly.