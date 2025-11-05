You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_25_code import factorize
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    import math
    fact = []
    i = 2
    while i <= int(math.sqrt(n) + 1):
        if n % i == 0:
            fact.append(i)
            n //= i
        else:
            i += 1

    if n > 1:
        fact.append(n)
    return fact


### Response:
Here is a unittest test script for the given Python function:


import unittest
from HumanEval_25_code import factorize

class TestFactorize(unittest.TestCase):
    def test_simple_numbers(self):
        self.assertEqual(factorize(1), [1])
        self.assertEqual(factorize(2), [2])
        self.assertEqual(factorize(3), [3])
        self.assertEqual(factorize(4), [2, 2])
        self.assertEqual(factorize(5), [5])
        self.assertEqual(factorize(6), [2, 3])
        self.assertEqual(factorize(7), [7])
        self.assertEqual(factorize(8), [2, 2, 2])
        self.assertEqual(factorize(9), [3, 3])
        self.assertEqual(factorize(10), [2, 5])

    def test_prime_numbers(self):
        self.assertEqual(factorize(11), [11])
        self.assertEqual(factorize(13), [13])
        self.assertEqual(factorize(17), [17])
        self.assertEqual(factorize(19), [19])
        self.assertEqual(factorize(23), [23])

    def test_composite_numbers(self):
        self.assertEqual(factorize(25), [5, 5])
        self.assertEqual(factorize(70), [2, 5, 7])
        self.assertEqual(factorize(100), [2, 2, 5, 5])
        self.assertEqual(factorize(101), [101])
        self.assertEqual(factorize(102), [2, 3, 17])

    def test_large_numbers(self):
        self.assertEqual(factorize(1000), [2, 2, 2, 5, 5, 5])
        self.assertEqual(factorize(10000), [2, 2, 2, 2, 5, 5, 5, 5])
        self.assertEqual(factorize(100000), [2, 2, 2, 2, 5, 5, 5, 5, 5, 5])

if __name__ == '__main__':
    unittest.main()


This script includes several test cases to ensure that the `factorize` function is working correctly. It tests with simple numbers, prime numbers, composite numbers, and large numbers. Each test case checks if the output of the `factorize` function matches the expected result.