You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_25_code import factorize

class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        with self.assertRaises(TypeError):
            factorize("string")
        with self.assertRaises(TypeError):
            factorize(1.5)
        with self.assertRaises(TypeError):
            factorize(False)

    def test_negative(self):
        with self.assertRaises(ValueError):
            factorize(-1)

    def test_zero_and_one_cases(self):
        self.assertEqual(factorize(0), [])
        self.assertEqual(factorize(1), [])

    def test_simple_numbers(self):
        self.assertEqual(factorize(3), [3])
        self.assertEqual(factorize(13), [13])

    def test_two_same_primes(self):
        self.assertEqual(factorize(4), [2, 2])
        self.assertEqual(factorize(25), [5, 5])

    def test_different_primes(self):
        self.assertEqual(factorize(30), [2, 3, 5])
        self.assertEqual(factorize(100), [2, 2, 5, 5])

    def test_big_numbers(self):
        self.assertEqual(factorize(1000), [2, 2, 2, 5, 5, 5])
        self.assertEqual(factorize(10000), [2, 2, 2, 2, 5, 5, 5, 5])

if __name__ == '__main__':
    unittest.main()


This suite includes tests for different types of inputs, including negative numbers, zero, one, simple numbers, numbers with two same primes, numbers with different primes, and big numbers.

Please note that the `HumanEval_25_code` module should contain the `factorize` function for these tests to work.