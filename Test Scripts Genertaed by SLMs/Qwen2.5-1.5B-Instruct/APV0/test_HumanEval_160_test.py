system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
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


assistant

import unittest

# Importing the function to be tested
from HumanEval_160_code import do_algebra

class TestDoAlgebra(unittest.TestCase):

    def test_addition(self):
        # Test case for addition operation
        operator = ['+']
        operand = [1, 2, 3]
        expected_result = 6
        self.assertEqual(do_algebra(operator, operand), expected_result)

    def test_subtraction(self):
        # Test case for subtraction operation
        operator = ['-']
        operand = [10, 5, 2]
        expected_result = 3
        self.assertEqual(do_algebra(operator, operand), expected_result)

    def test_multiplication(self):
        # Test case for multiplication operation
        operator = ['*']
        operand = [2, 3, 4]
        expected_result = 24
        self.assertEqual(do_algebra(operator, operand), expected_result)

    def test_floor_division(self):
        # Test case for floor division operation
        operator = ['//']
        operand = [8, 2, 3]
        expected_result = 2
        self.assertEqual(do_algebra(operator, operand), expected_result)

    def test_exponentiation(self):
        # Test case for exponentiation operation
        operator = ['**']
        operand = [2, 3, 2]
        expected_result = 8
        self.assertEqual(do_algebra(operator, operand), expected_result)

    def test_multiple_operators(self):
        # Test case with multiple operators
        operator = ['+', '**', '//']
        operand = [2, 3, 4, 5]
        expected_result = 2 + 3**4 - 5 // 2
        self.assertEqual(do_algebra(operator, operand), expected_result)

    def test_empty_operator(self):
        # Test case with empty operator list
        operator = []
        operand = [1, 2, 3]
        with self.assertRaises(ValueError):
            do_algebra(operator, operand)

    def test_incorrect_length(self):
        # Test case with incorrect length of operands
        operator = ['+', '*']
        operand = [1, 2, 3]
        with self.assertRaises(AssertionError):
            do_algebra(operator, operand)

    def test_negative_operand(self):
        # Test case with negative operand
        operator = ['-', '+']
        operand = [-1, 2, 3]
        expected_result = -1 - 2 + 3
        self.assertEqual(do_algebra(operator, operand), expected_result)

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` and defines a class `TestDoAlgebra` that inherits from `unittest.TestCase`. It includes several test cases to cover different scenarios as described in the problem statement. Each test case uses assertions to verify if the function behaves correctly under various conditions. If any assertion fails, it will raise an exception indicating which test failed. Finally, the script runs all tests when executed directly using `unittest.main()`.