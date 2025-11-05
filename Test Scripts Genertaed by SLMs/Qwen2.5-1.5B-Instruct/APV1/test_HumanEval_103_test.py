system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_103_code import rounded_avg
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """

    if m < n:
        return -1
    summation = 0
    for i in range(n, m + 1):
        summation += i
    return bin(round(summation / (m - n + 1)))


assistant

import unittest

# Function to be tested
from HumanEval_103_code import rounded_avg

class TestRoundAvg(unittest.TestCase):

    def test_rounded_avg(self):
        # Test cases provided in the problem description
        self.assertEqual(rounded_avg(1, 5), '0b11')
        self.assertEqual(rounded_avg(7, 5), -1)
        self.assertEqual(rounded_avg(10, 20), '0b1111')
        self.assertEqual(rounded_avg(20, 33), '0b11010')

    def test_invalid_input(self):
        # Test case where n > m
        self.assertEqual(rounded_avg(33, 20), -1)

    def test_zero_sum(self):
        # Test case where the sum of numbers between n and m is zero
        self.assertEqual(rounded_avg(4, 4), '0b0')

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `TestRoundAvg` class within the `unittest` module, which contains several test methods to ensure the correctness of the `rounded_avg` function. The test cases cover various scenarios as described in the problem statement, including valid inputs, invalid inputs (where `n` is greater than `m`), and edge cases like when the sum of numbers between `n` and `m` is zero.