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

 Here is a unittest test script for the given derivative function:


import unittest
from HumanEval_62_code import derivative

class TestDerivative(unittest.TestCase):

    def test_derivative(self):
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])
        self.assertEqual(derivative([1, 2, 3]), [2, 6])
        self.assertEqual(derivative([1]), [0])
        self.assertEqual(derivative([]), [])
        self.assertEqual(derivative([0]), [0])
        self.assertEqual(derivative([1, 0]), [0])

if __name__ == '__main__':
    unittest.main()


This test script includes multiple test cases for different inputs to ensure the function works as expected. You can run this script directly to test the derivative function.