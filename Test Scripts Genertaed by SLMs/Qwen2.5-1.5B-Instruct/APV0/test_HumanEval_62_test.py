system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Define the function to be tested
from HumanEval_62_code import derivative

class TestDerivative(unittest.TestCase):
    def test_derivative(self):
        # Test case 1
        self.assertEqual(derivative([3, 1, 2, 4, 5]), [1, 4, 12, 20])

        # Test case 2
        self.assertEqual(derivative([1, 2, 3]), [2, 6])

        # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a test class `TestDerivative` that inherits from `unittest.TestCase`. It includes a single test method `test_derivative` which uses assertions to check if the `derivative` function returns the expected results for given input polynomials. The `assertEqual` method is used to compare the output of the `derivative` function with the expected values. Finally, the script runs all tests when executed directly using `unittest.main()`.