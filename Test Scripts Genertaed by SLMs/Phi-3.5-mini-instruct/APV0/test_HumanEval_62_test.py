Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

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

 import unittest
from HumanEval_62_code import derivative

class TestDerivativeFunction(unittest.TestCase):

    def test_derivative_of_polynomial(self):
        # Test the derivative of a polynomial with multiple terms
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])

    def test_derivative_of_linear_polynomial(self):
        # Test the derivative of a linear polynomial
        self.assertEqual(derivative([1, 2]), [2])

    def test_derivative_of_constant_polynomial(self):
        # Test the derivative of a constant polynomial (should be 0)
        self.assertEqual(derivative([5]), [])

    def test_derivative_of_zero_coefficient_polynomial(self):
        # Test the derivative of a polynomial with a zero coefficient
        self.assertEqual(derivative([0, 3, 1]), [3])

    def test_derivative_with_empty_list(self):
        # Test the derivative with an empty list
        self.assertEqual(derivative([]), [])

    def test_derivative_with_single_term(self):
        # Test the derivative with a single term polynomial
        self.assertEqual(derivative([4]), [])

if __name__ == '__main__':
    unittest.main()