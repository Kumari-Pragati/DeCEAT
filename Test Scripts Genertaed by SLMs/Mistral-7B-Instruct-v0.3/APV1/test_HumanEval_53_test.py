You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_53_code import add

3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

 Here is a simple unittest test suite for the given Python function `add`. The test cases cover various scenarios, including positive numbers, negative numbers, and zero.


import unittest
from HumanEval_53_code import add

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)
        self.assertEqual(add(10, 20), 30)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-5, -7), -12)
        self.assertEqual(add(-10, -20), -30)

    def test_add_zero(self):
        self.assertEqual(add(0, 3), 3)
        self.assertEqual(add(-3, 0), -3)
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()


This test suite includes three test methods: `test_add_positive_numbers`, `test_add_negative_numbers`, and `test_add_zero`. Each method tests a specific scenario, and the `assertEqual` method is used to verify that the output of the `add` function matches the expected result.