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

 import unittest
from HumanEval_103_code import rounded_avg

class TestRoundedAverage(unittest.TestCase):

    def test_rounded_avg_with_increasing_range(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")

    def test_rounded_avg_with_decreasing_range(self):
        self.assertEqual(rounded_avg(7, 5), -1)

    def test_rounded_avg_with_equal_range(self):
        self.assertEqual(rounded_avg(10, 20), "0b1111")

    def test_rounded_avg_with_large_range(self):
        self.assertEqual(rounded_avg(20, 33), "0b11010")

    def test_rounded_avg_with_negative_result(self):
        self.assertEqual(rounded_avg(5, 1), -1)

    def test_rounded_avg_with_zero_range(self):
        self.assertEqual(rounded_avg(5, 5), "0b10")

    def test_rounded_avg_with_single_number(self):
        self.assertEqual(rounded_avg(1, 1), "0b1")

    def test_rounded_avg_with_no_range(self):
        self.assertEqual(rounded_avg(10, 10), "0b10")

if __name__ == '__main__':
    unittest.main()