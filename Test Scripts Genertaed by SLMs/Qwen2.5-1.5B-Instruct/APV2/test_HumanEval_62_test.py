system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


assistant

import unittest

# Function to be tested
from HumanEval_62_code import derivative

class TestDerivative(unittest.TestCase):

    def test_derivative(self):
        # Test cases based on provided examples
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

    def test_empty_list(self):
        # Test case for empty input list
        self.assertEqual(derivative([]), [])

    def test_single_element(self):
        # Test case for single element input list
        self.assertEqual(derivative([7]), [7])

if __name__ == '__main__':
    unittest.main()


This test suite includes three test methods:

- `test_derivative`: Tests the function with the provided examples.
- `test_empty_list`: Ensures the function handles an empty list correctly.
- `test_single_element`: Verifies that the function works with a single-element list.

The `unittest` framework will run these tests when executed directly or as part of another script.