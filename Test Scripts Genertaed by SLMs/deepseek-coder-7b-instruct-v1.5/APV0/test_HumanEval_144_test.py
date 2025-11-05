You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_144_code import simplify

class TestSimplify(unittest.TestCase):
    def test_simplify_true(self):
        self.assertTrue(simplify("1/5", "5/1"))

    def test_simplify_false(self):
        self.assertFalse(simplify("1/6", "2/1"))
        self.assertFalse(simplify("7/10", "10/2"))

    def test_simplify_invalid_input(self):
        with self.assertRaises(ValueError):
            simplify("1/0", "2/1")
        with self.assertRaises(ValueError):
            simplify("1/6", "2/0")
        with self.assertRaises(ValueError):
            simplify("1/0", "2/0")

if __name__ == '__main__':
    unittest.main()


This script tests the `simplify` function with different cases. It tests when the function should return True, when it should return False, and when it should raise a ValueError.

Please note that the `HumanEval_144_code` module should contain the `simplify` function for the tests to run correctly.

Also, please note that the `simplify` function checks if the multiplication of the numerators and denominators is a whole number. If the denominators are not whole numbers, the function will return False, even if the result of the multiplication is a whole number. This is because the function is checking if the fraction simplifies to a whole number, not if the multiplication is a whole number.