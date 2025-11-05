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
    return False

 Here is a unittest test script for the `simplify` function:


import unittest
from HumanEval_144_code import simplify

class TestSimplifyFunction(unittest.TestCase):
    def test_simplify(self):
        self.assertTrue(simplify("1/5", "5/1"))
        self.assertFalse(simplify("1/6", "2/1"))
        self.assertFalse(simplify("7/10", "10/2"))
        self.assertFalse(simplify("1/3", "4/1"))  # Test for a case where the result is not a whole number
        self.assertTrue(simplify("2/3", "6/1"))  # Test for a case where the result is a whole number but the fractions are not in reduced form
        self.assertFalse(simplify("1/2", "1/2"))  # Test for a case where the fractions are already simplified
        self.assertFalse(simplify("0/5", "5/1"))  # Test for a case where the denominator is zero
        self.assertFalse(simplify("1/0", "5/1"))  # Test for a case where the denominator is zero

if __name__ == '__main__':
    unittest.main()


This test script includes a test case for the edge case where the fractions are already simplified, as well as cases where the denominator is zero, which are not explicitly mentioned in the function description but should be handled appropriately to ensure the function behaves correctly in all scenarios.