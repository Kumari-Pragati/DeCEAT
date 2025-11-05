You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

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


### Response:
Here is the unittest test suite for the given function:


import unittest
from HumanEval_3_code import below_zero

class TestBelowZero(unittest.TestCase):
    def test_positive_operations(self):
        self.assertFalse(below_zero([1, 2, 3]))
        self.assertFalse(below_zero([10, 20, 30]))

    def test_negative_operations(self):
        self.assertTrue(below_zero([1, 2, -4, 5]))
        self.assertTrue(below_zero([10, -20, 30]))

    def test_mixed_operations(self):
        self.assertTrue(below_zero([1, -2, -3]))
        self.assertFalse(below_zero([10, -20, 30]))

    def test_empty_operations(self):
        self.assertFalse(below_zero([]))

    def test_zero_operations(self):
        self.assertFalse(below_zero([0, 0, 0]))

if __name__ == '__main__':
    unittest.main()


This suite includes tests for different scenarios:

- When all operations are positive and the balance never goes below zero.
- When some operations are negative and the balance goes below zero.
- When operations are mixed (some positive, some negative) and the balance goes below zero.
- When there are no operations (the list is empty).
- When all operations are zero (the balance remains zero).

Each test case checks a specific scenario and asserts the expected result.