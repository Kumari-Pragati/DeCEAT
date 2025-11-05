You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 Here is a comprehensive unittest test suite for the given Python function `factorize`.


import unittest
from HumanEval_25_code import factorize

class TestFactorize(unittest.TestCase):

    def test_factorize_simple_numbers(self):
        self.assertEqual(factorize(1), [])
        self.assertEqual(factorize(2), [2])
        self.assertEqual(factorize(3), [3])
        self.assertEqual(factorize(4), [2, 2])
        self.assertEqual(factorize(5), [5])
        self.assertEqual(factorize(6), [2, 3])
        self.assertEqual(factorize(7), [7])
        self.assertEqual(factorize(8), [2, 2, 2])
        self.assertEqual(factorize(9), [3, 3])

    def test_factorize_composite_numbers(self):
        self.assertEqual(factorize(10), [2, 5])
        self.assertEqual(factorize(15), [3, 5])
        self.assertEqual(factorize(20), [2, 2, 5])
        self.assertEqual(factorize(21), [3, 7])
        self.assertEqual(factorize(28), [2, 2, 7])
        self.assertEqual(factorize(45), [3, 3, 5])
        self.assertEqual(factorize(49), [7, 7])
        self.assertEqual(factorize(70), [2, 5, 7])
        self.assertEqual(factorize(81), [3, 3, 3, 3])

    def test_factorize_large_numbers(self):
        self.assertEqual(factorize(100), [2, 2, 5, 5, 11])
        self.assertEqual(factorize(1000), [2, 2, 2, 2, 5, 5, 5, 7, 11, 13])
        self.assertEqual(factorize(10000), [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2