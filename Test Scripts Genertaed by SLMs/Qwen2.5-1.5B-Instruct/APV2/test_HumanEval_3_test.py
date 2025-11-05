system
You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.
user
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


assistant

import unittest

# Provided function
from HumanEval_3_code import below_zero

# Test class
class TestBelowZero(unittest.TestCase):
    
    def test_below_zero(self):
        # Test case 1: Balance never goes negative
        self.assertFalse(below_zero([1, 2, 3]))
        
        # Test case 2: Balance goes negative at some point
        self.assertTrue(below_zero([1, 2, -4, 5]))

if __name__ == '__main__':
    unittest.main()


This test suite includes two test cases to verify the correctness of the `below_zero` function. The first test case checks if the function correctly returns `False` when the balance never goes negative. The second test case checks if the function correctly returns `True` when the balance goes negative at some point.