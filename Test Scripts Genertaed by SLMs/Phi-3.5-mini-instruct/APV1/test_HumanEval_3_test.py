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
    return False

 import unittest
from HumanEval_3_code import below_zero

class TestBelowZero(unittest.TestCase):

    def test_positive_operations(self):
        self.assertFalse(below_zero([1, 2, 3]))

    def test_negative_operations(self):
        self.assertTrue(below_zero([1, 2, -4, 5]))

    def test_zero_operations(self):
        self.assertFalse(below_zero([]))

    def test_single_negative_operation(self):
        self.assertTrue(below_zero([-1]))

    def test_multiple_negative_operations(self):
        self.assertTrue(below_zero([1, -2, -3, -4]))

    def test_balance_reaches_zero(self):
        self.assertFalse(below_zero([1, -1, 0, 1]))

    def test_balance_falls_below_zero_immediately(self):
        self.assertTrue(below_zero([-1, 1]))

    def test_balance_falls_below_zero_after_positive_operations(self):
        self.assertTrue(below_zero([1, 2, -5, 1]))

    def test_balance_remains_below_zero_after_negative_operations(self):
        self.assertTrue(below_zero([1, -2, -3, -4, -5]))

    def test_balance_never_falls_below_zero(self):
        self.assertFalse(below_zero([1, 2, 3, 4, 5]))

    def test_empty_list(self):
        self.assertFalse(below_zero([]))

    def test_list_with_only_positive_numbers(self):
        self.assertFalse(below_zero([1, 2, 3, 4, 5]))

    def test_list_with_only_negative_numbers(self):
        self.assertTrue(below_zero([-1, -2, -3, -4, -5]))

    def test_list_with_mixed_numbers(self):
        self.assertTrue(below_zero([1, -2, 3, -4, 5]))

if __name__ == '__main__':
    unittest.main()