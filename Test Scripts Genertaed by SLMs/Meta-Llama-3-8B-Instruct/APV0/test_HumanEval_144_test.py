user

Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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
    return Falseassistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_144_code import simplify

class TestSimplifyFunction(unittest.TestCase):

    def test_simplify(self):
        self.assertTrue(simplify("1/5", "5/1"))
        self.assertFalse(simplify("1/6", "2/1"))
        self.assertFalse(simplify("7/10", "10/2"))
        self.assertTrue(simplify("1/1", "1/1"))
        self.assertFalse(simplify("1/2", "1/3"))
        self.assertTrue(simplify("2/3", "3/2"))
        self.assertFalse(simplify("1/4", "1/5"))
        self.assertTrue(simplify("1/1", "1/1"))

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            simplify("1/0", "5/1")
        with self.assertRaises(ValueError):
            simplify("1/5", "5/0")

if __name__ == '__main__':
    unittest.main()


This script includes two test cases: `test_simplify` and `test_invalid_input`. The `test_simplify` function tests the `simplify` function with various inputs and expected outputs. The `test_invalid_input` function tests the function with invalid inputs (fractions with zero as denominator) and checks that it raises a `ValueError` as expected.