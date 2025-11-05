system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_160_code import do_algebra
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def do_algebra(operator, operand):
    """
    Given two lists — operator and operand — build an algebraic expression and return its evaluated result.

    The basic algebra operations:
        +  Addition  
        -  Subtraction  
        *  Multiplication  
        // Floor division  
        ** Exponentiation  

    Example:
        operator = ['+', '*', '-']
        operand = [2, 3, 4, 5]
        result = 2 + 3 * 4 - 5  → 9

    Notes:
        - len(operator) == len(operand) - 1
        - operand contains non-negative integers
        - operator has at least one element
    """
    expression = str(operand[0])
    for oprt, oprn in zip(operator, operand[1:]):
        expression += oprt + str(oprn)
    return eval(expression)


assistant

import unittest

# Provided function to be tested
from HumanEval_160_code import do_algebra

class TestDoAlgebra(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(do_algebra(['+'], [1, 2]), 3)

    def test_subtraction(self):
        self.assertEqual(do_algebra(['-', '*'], [10, 2, 3, 4]), 8)

    def test_multiplication(self):
        self.assertEqual(do_algebra(['*', '+', '-'], [2, 3, 4, 5]), 9)

    def test_floor_division(self):
        self.assertEqual(do_algebra(['//'], [10, 2, 3, 4]), 2)

    def test_exponentiation(self):
        self.assertEqual(do_algebra(['**'], [2, 3, 4, 5]), 32)

    def test_multiple_operands(self):
        self.assertEqual(do_algebra(['+', '-', '/'], [10, 2, 3, 4, 5]), 7)

    def test_empty_operator(self):
        with self.assertRaises(ValueError):
            do_algebra([], [])

    def test_incorrect_length(self):
        with self.assertRaises(AssertionError):
            do_algebra(['+'], [1, 2, 3])

    def test_negative_operand(self):
        with self.assertRaises(ValueError):
            do_algebra(['*'], [-1, 2, 3, 4])

    def test_zero_operand(self):
        with self.assertRaises(ValueError):
            do_algebra(['/'], [0])

if __name__ == '__main__':
    unittest.main()


This unittest test suite includes tests for various scenarios as described in the problem statement, ensuring that the `do_algebra` function behaves correctly under different conditions.