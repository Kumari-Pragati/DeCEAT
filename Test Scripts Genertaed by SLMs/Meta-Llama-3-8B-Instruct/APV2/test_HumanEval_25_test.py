system

You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.user

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
    return factassistant

Here is the complete unittest test suite for the given Python function:

Python
import unittest
from HumanEval_25_code import factorize

class TestFactorize(unittest.TestCase):

    def test_factorize_8(self):
        self.assertEqual(factorize(8), [2, 2, 2])

    def test_factorize_25(self):
        self.assertEqual(factorize(25), [5, 5])

    def test_factorize_70(self):
        self.assertEqual(factorize(70), [2, 5, 7])

    def test_factorize_1(self):
        self.assertEqual(factorize(1), [])

    def test_factorize_2(self):
        self.assertEqual(factorize(2), [2])

    def test_factorize_3(self):
        self.assertEqual(factorize(3), [3])

    def test_factorize_4(self):
        self.assertEqual(factorize(4), [2, 2])

    def test_factorize_5(self):
        self.assertEqual(factorize(5), [5])

    def test_factorize_6(self):
        self.assertEqual(factorize(6), [2, 3])

    def test_factorize_7(self):
        self.assertEqual(factorize(7), [7])

    def test_factorize_8_2(self):
        self.assertEqual(factorize(8*2), [2, 2, 2, 2])

    def test_factorize_8_3(self):
        self.assertEqual(factorize(8*3), [2, 2, 2, 2, 2, 2])

    def test_factorize_8_4(self):
        self.assertEqual(factorize(8*4), [2, 2, 2, 2, 2, 2, 2, 2])

    def test_factorize_8_5(self):
        self.assertEqual(factorize(8*5), [2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

    def test_factorize_8_6(self):
        self.assertEqual(factorize(8*6), [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

    def test_factorize_8_7(self):
        self.assertEqual(factorize(8*7), [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

    def test_factorize_8_8(self):
        self.assertEqual(factorize(8*8), [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

    def test_factorize_8_9(self):
        self.assertEqual(factorize(8*9), [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

    def test_factorize_8_10(self):
        self.assertEqual(factorize(8*10), [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

    def test_factorize_8_11(self):
        self.assertEqual(factorize(8*11), [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

    def test_factorize_8_12(self):
        self.assertEqual(factorize(8*12), [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

    def test_factorize_8_13(self):
        self.assertEqual(factorize(8*13), [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,