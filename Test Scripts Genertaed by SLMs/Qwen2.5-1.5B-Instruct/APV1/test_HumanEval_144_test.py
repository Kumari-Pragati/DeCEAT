system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_144_code import simplify
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def simplify(x, n):
    """Your task is to implement a function that will simplify the expression
    x * n. The function returns True if x * n evaluates to a whole number and False
    otherwise. Both x and n, are string representation of a fraction, and have the following format,
    <numerator>/<denominator> where both numerator and denominator are positive whole numbers.

    You can assume that x, and n are valid fractions, and do not have zero as denominator.

    simplify("1/5", "5/1") = True
    simplify("1/6", "2/1") = False
    simplify("7/10", "10/2") = False
    """
    a, b = x.split("/")
    c, d = n.split("/")
    numerator = int(a) * int(c)
    denom = int(b) * int(d)
    if (numerator / denom == int(numerator / denom)):
        return True
    return False


assistant

import unittest

# Function to be tested
from HumanEval_144_code import simplify

class TestSimplify(unittest.TestCase):

    def test_simplify(self):
        # Test cases provided in the problem description
        self.assertTrue(simplify("1/5", "5/1"))
        self.assertFalse(simplify("1/6", "2/1"))
        self.assertFalse(simplify("7/10", "10/2"))

    def test_invalid_input(self):
        # Test case with invalid input (e.g., non-fraction strings or negative denominators)
        self.assertRaises(ValueError, simplify, "-1/2", "2/-1")
        self.assertRaises(ValueError, simplify, "1/0", "1")

    def test_zero_denominator(self):
        # Test case with zero as the denominator
        self.assertFalse(simplify("1/2", "0/1"))

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `unittest` test suite for the `simplify` function. It includes three test methods:

1. `test_simplify`: Tests the function with the provided examples.
2. `test_invalid_input`: Checks for exceptions when the inputs are invalid.
3. `test_zero_denominator`: Ensures the function handles zero denominators correctly.

The `unittest.main()` call at the end runs all the tests defined in the class.