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

 Here is a comprehensive unittest test suite for the `rounded_avg` function:


import unittest
from HumanEval_103_code import rounded_avg

class TestRoundedAvg(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")
        self.assertEqual(rounded_avg(7, 5), -1)
        self.assertEqual(rounded_avg(10, 20), "0b1111")
        self.assertEqual(rounded_avg(20, 33), "0b11010")
        self.assertEqual(rounded_avg(1, 1), "0b1")
        self.assertEqual(rounded_avg(100, 150), "0b1111100")

    def test_edge_cases(self):
        self.assertEqual(rounded_avg(1, 0), -1)
        self.assertEqual(rounded_avg(0, 1), "0b1")
        self.assertEqual(rounded_avg(1, 1000000), "0b1")
        self.assertEqual(rounded_avg(1000000, 1), "0b1")

    def test_invalid_input(self):
        self.assertEqual(rounded_avg(-1, 1), -1)
        self.assertEqual(rounded_avg(1, -1), -1)
        self.assertEqual(rounded_avg(0, 0), -1)
        self.assertEqual(rounded_avg(1, 0.5), -1)
        self.assertEqual(rounded_avg(0.5, 1), -1)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for valid inputs, edge cases, and invalid inputs. It covers a wide range of test cases to ensure the `rounded_avg` function works correctly under various conditions.