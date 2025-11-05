You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_62_code import derivative

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def derivative(xs: list):
    """xs represent coefficients of a polynomial.
    xs[0] + xs[1] * x + xs[2] * x^2 + ....
    Return derivative of this polynomial in the same form.
    >>> derivative([3, 1, 2, 4, 5])
    [1, 4, 12, 20]
    >>> derivative([1, 2, 3])
    [2, 6]
    """
    return [(i * x) for i, x in enumerate(xs)][1:]

 Here is a comprehensive unittest test suite for the given Python function:


import unittest
from HumanEval_62_code import derivative

class TestDerivative(unittest.TestCase):

    def test_derivative_simple(self):
        self.assertEqual(derivative([3]), [0])
        self.assertEqual(derivative([1]), [0])
        self.assertEqual(derivative([0]), [0])

    def test_derivative_one_term(self):
        self.assertEqual(derivative([1]), [0, 1])
        self.assertEqual(derivative([2]), [0, 2])
        self.assertEqual(derivative([-1]), [0, -1])

    def test_derivative_two_terms(self):
        self.assertEqual(derivative([1, 2]), [2, 2])
        self.assertEqual(derivative([2, 1]), [2, 1])
        self.assertEqual(derivative([-1, 2]), [-2, 2])

    def test_derivative_multiple_terms(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])
        self.assertEqual(derivative([1, 2, 3, 4, 5]), [2, 6, 12, 20, 30])
        self.assertEqual(derivative([-1, 2, -3, 4, -5]), [-2, -6, 12, -20, 30])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the edge cases, single term, two terms, and multiple terms. It covers both positive and negative coefficients.