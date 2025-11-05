You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_97_code import multiply

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.

    Examples:
    multiply(148, 412) ➞ 16
    multiply(19, 28) ➞ 72
    multiply(2020, 1851) ➞ 0
    multiply(14, -15) ➞ 20
    """

    return abs(a % 10) * abs(b % 10)

 Here is a simple unittest test suite for the given Python function:


import unittest
from HumanEval_97_code import multiply

class TestMultiplyFunction(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)
        self.assertEqual(multiply(2020, 1851), 0)
        self.assertEqual(multiply(14, -15), 20)
        self.assertEqual(multiply(-148, 412), 16)
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(1, 0), 0)
        self.assertEqual(multiply(0, 1), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes several test cases for different input scenarios, including negative numbers, zero, and multiplication of zero. The test cases use the `assertEqual` method to check if the expected output matches the actual output of the function.