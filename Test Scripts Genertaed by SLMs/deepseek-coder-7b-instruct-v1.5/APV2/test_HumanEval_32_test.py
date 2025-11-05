You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_32_code import find_zero

class TestFindZero(unittest.TestCase):

    def test_linear_polynomial(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=2)

    def test_quadratic_polynomial(self):
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=2)

    def test_cubic_polynomial(self):
        self.assertAlmostEqual(find_zero([2, -6, 8, -6, 2]), 1.0, places=2)

    def test_negative_coefficients(self):
        self.assertAlmostEqual(find_zero([-1, 2, -1]), 1.0, places=2)

    def test_large_coefficients(self):
        self.assertAlmostEqual(find_zero([1000000, -2000000, 1000000]), 1.0, places=2)

    def test_zero_polynomial(self):
        self.assertEqual(find_zero([0]), None)

    def test_single_coefficient_polynomial(self):
        self.assertEqual(find_zero([1]), 0)

    def test_even_number_of_coefficients(self):
        with self.assertRaises(ValueError):
            find_zero([1, 2, 3])

if __name__ == '__main__':
    unittest.main()


This suite includes tests for various scenarios, including linear, quadratic, and cubic polynomials, polynomials with negative coefficients, polynomials with large coefficients, and edge cases such as a zero polynomial and a polynomial with only one coefficient. It also checks that an error is raised when the input list has an odd number of coefficients, which is not a valid input for the `find_zero` function.