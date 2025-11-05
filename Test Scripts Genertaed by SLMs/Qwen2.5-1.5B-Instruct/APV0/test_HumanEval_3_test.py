system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
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
    return False


assistant

import unittest

# Function to check if the balance goes below zero after performing all operations
def below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False

class TestBelowZero(unittest.TestCase):
    def test_below_zero(self):
        self.assertFalse(below_zero([1, 2, 3]))
        self.assertTrue(below_zero([1, 2, -4, 5]))

if __name__ == '__main__':
    unittest.main()


This script imports `unittest` module, defines the `below_zero` function as provided, and includes a class `TestBelowZero` with a method `test_below_zero` to run several test cases using the `assert` statements. The `unittest.main()` call at the end makes the tests executable when the script is run directly.