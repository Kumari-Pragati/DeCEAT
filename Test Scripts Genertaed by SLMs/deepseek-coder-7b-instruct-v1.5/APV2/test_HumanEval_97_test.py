You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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
Here is the unittest test suite for the given function:


import unittest
from HumanEval_97_code import multiply

class TestMultiply(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)
        self.assertEqual(multiply(2020, 1851), 0)

    def test_negative_numbers(self):
        self.assertEqual(multiply(-14, -15), 20)
        self.assertEqual(multiply(-14, 15), 20)
        self.assertEqual(multiply(14, -15), 20)

    def test_mixed_numbers(self):
        self.assertEqual(multiply(-148, 412), 16)
        self.assertEqual(multiply(19, -28), 72)
        self.assertEqual(multiply(-2020, 1851), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive numbers, negative numbers, and mixed numbers. It checks if the function returns the correct product of their unit digits for all these cases.