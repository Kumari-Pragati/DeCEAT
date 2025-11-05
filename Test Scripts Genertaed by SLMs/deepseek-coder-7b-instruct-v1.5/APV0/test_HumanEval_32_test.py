You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
Here is a unittest script for the given Python function:


import unittest
from HumanEval_32_code import find_zero

class TestFindZero(unittest.TestCase):

    def test_linear_polynomial(self):
        self.assertAlmostEqual(find_zero([1, 2]), -0.5, places=2)

    def test_quadratic_polynomial(self):
        self.assertAlmostEqual(find_zero([-6, 11, -6, 1]), 1.0, places=2)

    def test_negative_coefficients(self):
        self.assertAlmostEqual(find_zero([-1, -2]), 1.0, places=2)

    def test_odd_number_of_coefficients(self):
        with self.assertRaises(ValueError):
            find_zero([1, 2, 3])

    def test_even_number_of_coefficients(self):
        self.assertAlmostEqual(find_zero([1, 2, 3, 0]), 0.5, places=2)

if __name__ == '__main__':
    unittest.main()


This script tests the `find_zero` function with different types of input, including linear and quadratic polynomials, polynomials with negative coefficients, and polynomials with an odd number of coefficients. It also tests the function's ability to handle errors properly by checking if it raises a `ValueError` when given an odd number of coefficients.