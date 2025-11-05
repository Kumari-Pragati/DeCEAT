You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_32_code import find_zero

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
import math


def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    return xs[0] + xs[1] * x + xs[2] * x^2 + .... + xs[n] * x^n
    """
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    """ xs are coefficients of a polynomial.
    find_zero finds x such that poly(x) = 0.
    find_zero returns only one zero point, even if there are many.
    Moreover, find_zero only takes list xs having even number of coefficients
    and largest non zero coefficient as it guarantees
    a solution.
    >>> round(find_zero([1, 2]), 2) # f(x) = 1 + 2x
    -0.5
    >>> round(find_zero([-6, 11, -6, 1]), 2) # (x - 1) * (x - 2) * (x - 3) = -6 + 11x - 6x^2 + x^3
    1.0
    """
    begin, end = -1.0, 1.0
    while poly(xs, begin) * poly(xs, end) > 0:
        begin *= 2.0
        end *= 2.0
    while end - begin > 1e-10:
        center = (begin + end) / 2.0
        if poly(xs, center) * poly(xs, begin) > 0:
            begin = center
        else:
            end = center
    return begin

 Here is a comprehensive unittest test suite for the `find_zero` function:


import unittest
from HumanEval_32_code import find_zero

class TestFindZero(unittest.TestCase):

    def test_find_zero_simple(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, delta=0.01)

    def test_find_zero_quadratic(self):
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, delta=0.01)

    def test_find_zero_higher_degree(self):
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1, 0]), 1.0, delta=0.01)

    def test_find_zero_negative_coefficients(self):
        self.assertAlmostEqual(find_zero([-1, -2]), 1.0, delta=0.01)

    def test_find_zero_zero_coefficients(self):
        self.assertEqual(find_zero([0]), None)

    def test_find_zero_odd_degree(self):
        with self.assertRaises(ValueError):
            find_zero([1, 2, 3])

if __name__ == '__main__':
    unittest.main()


This test suite includes various test cases for different scenarios, such as simple linear equations, quadratic equations, higher-degree equations, negative coefficients, zero coefficients, and odd-degree polynomials (which are not supported by the function). The `assertAlmostEqual` function is used to compare the expected output with the actual output, allowing for a small tolerance (delta) to account for floating-point errors. The `assertRaises` function is used to test for exceptions that should be raised in certain cases.