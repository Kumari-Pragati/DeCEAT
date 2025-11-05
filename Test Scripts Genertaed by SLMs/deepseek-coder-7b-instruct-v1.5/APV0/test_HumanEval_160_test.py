You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_160_code import do_algebra

class TestDoAlgebra(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(do_algebra(['+'], [2, 3]), 5)
        self.assertEqual(do_algebra(['+', '+'], [2, 3, 4]), 9)

    def test_subtraction(self):
        self.assertEqual(do_algebra(['-'], [5, 2]), 3)
        self.assertEqual(do_algebra(['-', '-'], [5, 2, 1]), 2)

    def test_multiplication(self):
        self.assertEqual(do_algebra(['*'], [2, 3]), 6)
        self.assertEqual(do_algebra(['*', '*'], [2, 3, 4]), 24)

    def test_floor_division(self):
        self.assertEqual(do_algebra(['//'], [6, 2]), 3)
        self.assertEqual(do_algebra(['//', '//'], [6, 2, 1]), 3)

    def test_exponentiation(self):
        self.assertEqual(do_algebra(['**'], [2, 3]), 8)
        self.assertEqual(do_algebra(['**', '**'], [2, 3, 2]), 64)

    def test_mixed_operations(self):
        self.assertEqual(do_algebra(['+', '-', '*'], [2, 3, 1, 2]), 0)
        self.assertEqual(do_algebra(['+', '-', '*', '//'], [10, 2, 3, 1, 2]), 3)

if __name__ == '__main__':
    unittest.main()


This script includes tests for each of the basic algebra operations (addition, subtraction, multiplication, floor division, and exponentiation) as well as a test for a mixed set of operations. It checks that the function returns the expected result for each test case.

Please note that this script assumes that the `HumanEval_160_code.do_algebra` function is available and that it behaves as described in the function's docstring. If the function is not behaving as expected, the tests may fail, even if the function is correct.