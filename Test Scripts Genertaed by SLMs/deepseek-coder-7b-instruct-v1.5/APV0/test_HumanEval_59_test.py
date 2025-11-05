You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here's a unittest script for the largest_prime_factor function:


import unittest
from HumanEval_59_code import largest_prime_factor

class TestLargestPrimeFactor(unittest.TestCase):
    def test_largest_prime_factor(self):
        self.assertEqual(largest_prime_factor(13195), 29)
        self.assertEqual(largest_prime_factor(2048), 2)
        self.assertEqual(largest_prime_factor(6), 3)
        self.assertEqual(largest_prime_factor(100), 5)
        self.assertEqual(largest_prime_factor(101), 101)
        self.assertEqual(largest_prime_factor(10000), 5)
        self.assertEqual(largest_prime_factor(100000000), 10000)

if __name__ == '__main__':
    unittest.main()


This script creates a TestLargestPrimeFactor class that inherits from unittest.TestCase. It includes a test_largest_prime_factor method that tests the largest_prime_factor function with various inputs. The unittest.main() call at the end runs the tests.

Please note that the function largest_prime_factor is not optimized for large inputs. It has a time complexity of O(n^2), which could be improved to O(n log n) or O(n) by using a different algorithm.