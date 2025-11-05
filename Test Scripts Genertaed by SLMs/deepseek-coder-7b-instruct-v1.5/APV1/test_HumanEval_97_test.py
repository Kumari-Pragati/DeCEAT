You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_97_code import multiply

class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)
        self.assertEqual(multiply(2020, 1851), 0)
        self.assertEqual(multiply(14, -15), 20)

    def test_negative_numbers(self):
        self.assertEqual(multiply(-148, -412), 16)
        self.assertEqual(multiply(-19, -28), 72)
        self.assertEqual(multiply(-2020, -1851), 0)
        self.assertEqual(multiply(-14, 15), 20)

    def test_mixed_numbers(self):
        self.assertEqual(multiply(-148, 412), 16)
        self.assertEqual(multiply(-19, 28), 72)
        self.assertEqual(multiply(-2020, 1851), 0)
        self.assertEqual(multiply(-14, -15), 20)

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_positive_numbers`: Tests the function with positive numbers.
2. `test_negative_numbers`: Tests the function with negative numbers.
3. `test_mixed_numbers`: Tests the function with a mix of positive and negative numbers.

Each test case checks the function's output against the expected result using the `assertEqual` method.

Please note that the function `multiply` is imported from the module `HumanEval_97_code`. Make sure that the function is defined in that module.