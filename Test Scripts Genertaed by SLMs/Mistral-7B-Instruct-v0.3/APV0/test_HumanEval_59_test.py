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

 Here is a unittest test script for the `largest_prime_factor` function. The test cases cover various inputs, including prime numbers, composite numbers, and edge cases.


import unittest
from HumanEval_59_code import largest_prime_factor

class TestLargestPrimeFactor(unittest.TestCase):

    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)
        self.assertEqual(largest_prime_factor(10), 5)
        self.assertEqual(largest_prime_factor(2), 2)
        self.assertEqual(largest_prime_factor(31), 31)
        self.assertEqual(largest_prime_factor(4), 2)
        self.assertEqual(largest_prime_factor(1), 1)
        self.assertEqual(largest_prime_factor(0), 0)
        self.assertEqual(largest_prime_factor(-1), 1)

if __name__ == '__main__':
    unittest.main()


This script defines a test case class `TestLargestPrimeFactor` with a method `test_largest_prime_factor` that tests the `largest_prime_factor` function. The unittest framework will run the test cases when the script is executed.