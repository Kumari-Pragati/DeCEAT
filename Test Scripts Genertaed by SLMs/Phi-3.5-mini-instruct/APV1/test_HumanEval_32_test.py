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

 import unittest
from HumanEval_32_code import find_zero, poly
import math

class TestFindZero(unittest.TestCase):

    def test_find_zero_with_simple_polynomial(self):
        # Test with a simple polynomial: f(x) = 1 + 2x
        coeffs = [1, 2]
        expected = -0.5
        self.assertAlmostEqual(find_zero(coeffs), expected, places=2)

    def test_find_zero_with_quadratic_polynomial(self):
        # Test with a quadratic polynomial: (x - 1) * (x - 2) * (x - 3)
        coeffs = [-6, 11, -6, 1]
        expected = 1.0
        self.assertAlmostEqual(find_zero(coeffs), expected, places=2)

    def test_find_zero_with_negative_coefficients(self):
        # Test with negative coefficients
        coeffs = [-1, 0, 1]
        expected = 0.0
        self.assertAlmostEqual(find_zero(coeffs), expected, places=2)

    def test_find_zero_with_even_number_of_coefficients(self):
        # Test with an even number of coefficients
        coeffs = [1, -3, 2, -1]
        expected = 1.0
        self.assertAlmostEqual(find_zero(coeffs), expected, places=2)

    def test_find_zero_with_large_non_zero_coefficient(self):
        # Test with the largest non-zero coefficient being 10
        coeffs = [10, -100, 1000, -10000, 100000]
        expected = 0.0
        self.assertAlmostEqual(find_zero(coeffs), expected, places=2)

    def test_find_zero_with_no_real_roots(self):
        # Test with a polynomial that has no real roots
        coeffs = [1, 0, 0, -1]
        with self.assertRaises(ValueError):
            find_zero(coeffs)

    def test_find_zero_with_invalid_input(self):
        # Test with an invalid input (non-list or list with odd number of coefficients)
        with self.assertRaises(TypeError):
            find_zero("not a list")
        with self.assertRaises(ValueError):
            find_zero([1, 2, 3])

if __name__ == '__main__':
    unittest.main()