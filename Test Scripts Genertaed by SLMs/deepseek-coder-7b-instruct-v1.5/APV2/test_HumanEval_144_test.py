You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is a unittest test suite for the simplify function:


import unittest
from HumanEval_144_code import simplify

class TestSimplify(unittest.TestCase):

    def test_whole_number_result(self):
        self.assertTrue(simplify("1/5", "5/1"))
        self.assertTrue(simplify("1/6", "2/1"))
        self.assertFalse(simplify("7/10", "10/2"))

    def test_fraction_result(self):
        self.assertFalse(simplify("1/2", "1/3"))
        self.assertFalse(simplify("1/4", "1/4"))

    def test_zero_denominator(self):
        with self.assertRaises(ZeroDivisionError):
            simplify("1/0", "1/1")

    def test_invalid_fraction(self):
        with self.assertRaises(ValueError):
            simplify("1/a", "1/1")
        with self.assertRaises(ValueError):
            simplify("a/1", "1/1")

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for when the result is a whole number, when the result is a fraction, when the denominator is zero, and when the input is an invalid fraction. The tests use the assertTrue and assertFalse methods to check that the function returns the correct boolean value. The test_zero_denominator test uses the assertRaises method to check that the function raises a ZeroDivisionError when the denominator is zero. The test_invalid_fraction tests use the assertRaises method to check that the function raises a ValueError when the input is an invalid fraction.