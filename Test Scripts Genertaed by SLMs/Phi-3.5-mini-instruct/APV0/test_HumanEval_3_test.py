Generate a unittest test script for the following Python function. 
The script should fully test the function and be runnable directly.

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
    return False

 import unittest
from HumanEval_3_code import below_zero

class TestBelowZero(unittest.TestCase):

    def test_positive_operations(self):
        self.assertFalse(below_zero([1, 2, 3]))

    def test_negative_operation_with_positive_operations(self):
        self.assertTrue(below_zero([1, 2, -4, 5]))

    def test_zero_balance_operations(self):
        self.assertFalse(below_zero([0, 0, 0]))

    def test_negative_balance_operations(self):
        self.assertTrue(below_zero([-1, 1, 1, 1]))

    def test_multiple_negative_operations(self):
        self.assertTrue(below_zero([-1, -1, -1, -1]))

    def test_zero_balance_after_negative_operations(self):
        self.assertTrue(below_zero([-1, -1, 1, 1]))

    def test_negative_balance_after_multiple_negative_operations(self):
        self.assertTrue(below_zero([-1, -1, -1, -1, 1, 1]))

    def test_no_operations(self):
        self.assertFalse(below_zero([]))

if __name__ == '__main__':
    unittest.main()