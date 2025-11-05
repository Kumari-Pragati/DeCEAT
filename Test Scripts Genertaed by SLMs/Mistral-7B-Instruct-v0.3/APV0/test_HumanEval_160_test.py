Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `do_algebra` function. The test cases cover various scenarios, including different operators and operand values, edge cases, and incorrect input.


import unittest
from HumanEval_160_code import do_algebra

class TestDoAlgebra(unittest.TestCase):

    def test_basic_algebra(self):
        operator = ['+', '*', '-']
        operand = [2, 3, 4, 5]
        result = 2 + 3 * 4 - 5
        self.assertEqual(do_algebra(operator, operand), result)

    def test_single_operator(self):
        operator = ['+']
        operand = [2, 3]
        result = 2 + 3
        self.assertEqual(do_algebra(operator, operand), result)

    def test_single_operand(self):
        operator = ['+', '-', '*', '//', '**']
        operand = [2]
        with self.assertRaises(ValueError):
            do_algebra(operator, operand)

    def test_empty_operator(self):
        operator = []
        operand = [2, 3, 4, 5]
        with self.assertRaises(ValueError):
            do_algebra(operator, operand)

    def test_incorrect_operand(self):
        operator = ['+', '-', '*', '//', '**']
        operand = [-1, 3, 4, 5]
        with self.assertRaises(ValueError):
            do_algebra(operator, operand)

    def test_incorrect_length(self):
        operator = ['+', '-', '*', '//', '**']
        operand = [2, 3, 4]
        with self.assertRaises(ValueError):
            do_algebra(operator, operand)

if __name__ == '__main__':
    unittest.main()


This test script includes tests for the basic algebra operation, single operator, single operand, empty operator, incorrect operand, incorrect length, and edge cases.