You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is a complete unittest test suite for the given Python function:


import unittest
from HumanEval_53_code import add

class TestAddFunction(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(-5, -7), -12)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(5, -7), -2)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(0, 5), 5)
        self.assertEqual(add(7, 0), 7)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for adding positive numbers, negative numbers, mixed numbers, and zero. It uses the `assertEqual` method to check if the result of the `add` function matches the expected result.