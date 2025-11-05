You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

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

 Here is a complete unittest test suite for the `do_algebra` function:


import unittest
from HumanEval_160_code import do_algebra

class TestDoAlgebra(unittest.TestCase):

    def test_do_algebra_simple_case(self):
        operator = ['+', '*', '-']
        operand = [2, 3, 4, 5]
        result = 2 + 3 * 4 - 5
        self.assertEqual(do_algebra(operator, operand), result)

    def test_do_algebra_empty_operator(self):
        with self.assertRaises(ValueError):
            do_algebra([], [1, 2, 3, 4])

    def test_do_algebra_operator_length(self):
        with self.assertRaises(ValueError):
            do_algebra(['+', '*'], [1, 2, 3, 4, 5])

    def test_do_algebra_negative_operand(self):
        with self.assertRaises(ValueError):
            do_algebra(['+', '-'], [-1, 2])

    def test_do_algebra_empty_operand(self):
        with self.assertRaises(ValueError):
            do_algebra(['+'], [])

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for the following cases:

1. Simple case where the function works correctly with a given operator and operand.
2. Empty operator list.
3. Operator list length is not equal to the length of the operand list minus 1.
4. Operand list contains negative integers.
5. Empty operand list.