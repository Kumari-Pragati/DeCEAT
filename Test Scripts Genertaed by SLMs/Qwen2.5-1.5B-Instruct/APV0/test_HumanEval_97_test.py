system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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


assistant

import unittest

# Importing the function to be tested
from HumanEval_97_code import multiply

class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)
        self.assertEqual(multiply(2020, 1851), 0)
        self.assertEqual(multiply(14, -15), 20)
        self.assertEqual(multiply(-14, 15), 20)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(123, 456), 18)
        self.assertEqual(multiply(1234, 5678), 25)

if __name__ == '__main__':
    unittest.main()


This script imports the `multiply` function and defines a class `TestMultiply` within the `unittest` module. It contains several test cases using assertEqual methods to verify the correctness of the `multiply` function against provided data points. The `if __name__ == '__main__':` block ensures that when this script is run as the main program, it will execute all the tests defined in the `TestMultiply` class.