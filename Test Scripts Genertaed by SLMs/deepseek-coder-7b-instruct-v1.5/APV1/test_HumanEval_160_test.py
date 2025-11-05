You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_160_code import do_algebra

class TestDoAlgebra(unittest.TestCase):

    def test_addition(self):
        operator = ['+']
        operand = [2, 3]
        self.assertEqual(do_algebra(operator, operand), 5)

    def test_subtraction(self):
        operator = ['-']
        operand = [5, 2]
        self.assertEqual(do_algebra(operator, operand), 3)

    def test_multiplication(self):
        operator = ['*']
        operand = [2, 3]
        self.assertEqual(do_algebra(operator, operand), 6)

    def test_floor_division(self):
        operator = ['//']
        operand = [6, 2]
        self.assertEqual(do_algebra(operator, operand), 3)

    def test_exponentiation(self):
        operator = ['**']
        operand = [2, 3]
        self.assertEqual(do_algebra(operator, operand), 8)

    def test_multiple_operations(self):
        operator = ['+', '*', '-', '//', '**']
        operand = [2, 3, 4, 5, 6]
        self.assertEqual(do_algebra(operator, operand), 12)

    def test_negative_operand(self):
        operator = ['+']
        operand = [2, -3]
        self.assertEqual(do_algebra(operator, operand), -1)

    def test_zero_operand(self):
        operator = ['+']
        operand = [2, 0]
        self.assertEqual(do_algebra(operator, operand), 2)

if __name__ == '__main__':
    unittest.main()


This suite includes tests for basic arithmetic operations, multiple operations in sequence, negative operands, and zero as an operand. It checks if the function correctly evaluates the algebraic expression built from the operator and operand lists.