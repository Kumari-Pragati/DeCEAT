user

You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_3_code import below_zero
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
from typing import List


def below_zero(operations: List[int]) -> bool:
    """You're given a list of deposit and withdrawal operations on a bank account that
    starts with zero balance. Your task is to detect if at any point the balance of
    account falls below zero, and at that point function should return True.
    Otherwise, it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return Falseassistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_3_code import below_zero

class TestBelowZero(unittest.TestCase):

    def test_positive_operations(self):
        self.assertFalse(below_zero([1, 2, 3]))

    def test_negative_operations(self):
        self.assertTrue(below_zero([1, 2, -4, 5]))

    def test_negative_operations_start(self):
        self.assertTrue(below_zero([-1, -2, -3]))

    def test_positive_operations_start(self):
        self.assertFalse(below_zero([1, 2, 3, 4]))

    def test_mixed_operations(self):
        self.assertTrue(below_zero([1, -2, 3, -4]))

    def test_zero_operations(self):
        self.assertFalse(below_zero([]))

    def test_single_operation(self):
        self.assertFalse(below_zero([1]))

    def test_negative_single_operation(self):
        self.assertTrue(below_zero([-1]))

    def test_multiple_negative_operations(self):
        self.assertTrue(below_zero([-1, -2, -3, -4]))

    def test_multiple_positive_operations(self):
        self.assertFalse(below_zero([1, 2, 3, 4, 5]))

if __name__ == '__main__':
    unittest.main()


This test suite covers a variety of scenarios, including:

- Positive operations only
- Negative operations only
- Mixed positive and negative operations
- Zero operations
- Single operation (positive and negative)
- Multiple positive and negative operations

Each test case is designed to verify the expected output of the `below_zero` function.