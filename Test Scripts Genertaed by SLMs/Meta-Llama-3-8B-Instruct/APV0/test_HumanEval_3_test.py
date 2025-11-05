user

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
    return Falseassistant

Here is the unittest test script for the `below_zero` function:

import unittest
from HumanEval_3_code import below_zero

class TestBelowZero(unittest.TestCase):
    def test_positive_operations(self):
        self.assertFalse(below_zero([1, 2, 3]))

    def test_negative_operations(self):
        self.assertTrue(below_zero([1, 2, -4, 5]))

    def test_mixed_operations(self):
        self.assertTrue(below_zero([1, -2, 3, -4, 5]))

    def test_all_positive_operations(self):
        self.assertFalse(below_zero([1, 2, 3, 4, 5]))

    def test_all_negative_operations(self):
        self.assertTrue(below_zero([-1, -2, -3, -4, -5]))

    def test_single_operation(self):
        self.assertFalse(below_zero([1]))

    def test_zero_operations(self):
        self.assertFalse(below_zero([]))

    def test_single_negative_operation(self):
        self.assertTrue(below_zero([-1]))

if __name__ == '__main__':
    unittest.main()

This test script covers a variety of scenarios to ensure the `below_zero` function is working correctly. It tests:

1. Positive operations only
2. Negative operations only
3. Mixed positive and negative operations
4. All positive operations
5. All negative operations
6. Single positive operation
7. Zero operations (i.e., an empty list)

Each test case uses the `assertFalse` or `assertTrue` method to verify the expected output of the `below_zero` function.