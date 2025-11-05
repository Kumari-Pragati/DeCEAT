Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the `rounded_avg` function:


import unittest
from HumanEval_103_code import rounded_avg

class TestRoundedAvg(unittest.TestCase):

    def test_rounded_avg_simple(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")
        self.assertEqual(rounded_avg(7, 5), -1)
        self.assertEqual(rounded_avg(10, 20), "0b1111")
        self.assertEqual(rounded_avg(20, 33), "0b11010")
        self.assertEqual(rounded_avg(34, 45), "0b101011")
        self.assertEqual(rounded_avg(46, 57), "0b1101111")
        self.assertEqual(rounded_avg(58, 69), "0b1110111")
        self.assertEqual(rounded_avg(70, 81), "0b1111011")
        self.assertEqual(rounded_avg(82, 93), "0b1111101")
        self.assertEqual(rounded_avg(94, 105), "0b1111110")

    def test_rounded_avg_edge_cases(self):
        self.assertEqual(rounded_avg(1, 1), "0b1")
        self.assertEqual(rounded_avg(2, 2), "0b10")
        self.assertEqual(rounded_avg(3, 3), "0b11")
        self.assertEqual(rounded_avg(4, 4), "0b100")
        self.assertEqual(rounded_avg(5, 5), "0b101")

    def test_rounded_avg_large_numbers(self):
        self.assertEqual(rounded_avg(1000000, 1000005), "0b11111111111111111111111111111111")
        self.assertEqual(rounded_avg(1000006, 1000005), -1)

    def test_rounded_avg_negative_numbers(self):
        self.assertEqual(rounded_avg(-1, -5), "0b1010")
        self.assertEqual(rounded_avg(-7, -5), -1)
        self.assertEqual(rounded_avg(-10, -20), "0b1111")
        self.assertEqual(rounded_avg(-20, -33), "0b11010")

if __name__ == '__main__':
    unittest.main()


This test script includes various test cases for different scenarios, such as simple cases, edge cases, large numbers, and negative numbers. It covers a wide range of test cases to ensure the function works correctly.