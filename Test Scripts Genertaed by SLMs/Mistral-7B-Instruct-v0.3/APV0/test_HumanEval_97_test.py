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

 Here is a simple unittest test script for the provided `multiply` function. I've included several test cases to cover various scenarios, including negative numbers and edge cases.


import unittest
from HumanEval_97_code import multiply

class TestMultiplyFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(multiply(148, 412), 16)
        self.assertEqual(multiply(19, 28), 72)

    def test_zero(self):
        self.assertEqual(multiply(2020, 1851), 0)

    def test_negative_numbers(self):
        self.assertEqual(multiply(14, -15), 20)
        self.assertEqual(multiply(-14, 15), 20)

    def test_edge_cases(self):
        self.assertEqual(multiply(10, 10), 10)
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(10, 0), 0)

if __name__ == '__main__':
    unittest.main()


This test script defines a `TestMultiplyFunction` class that contains several test methods. Each test method checks a specific scenario, and the `assertEqual` method is used to verify that the expected and actual results match. The `unittest.main()` function is called at the end to run the tests.