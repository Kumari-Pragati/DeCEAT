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
    return bin(round(summation / (m - n + 1)))assistant

Here is a comprehensive unittest test suite for the given Python function:

Python
import unittest
from HumanEval_103_code import rounded_avg

class TestRoundedAvg(unittest.TestCase):

    def test_rounded_avg_positive(self):
        self.assertEqual(rounded_avg(1, 5), "0b11")
        self.assertEqual(rounded_avg(10, 20), "0b1111")
        self.assertEqual(rounded_avg(20, 33), "0b11010")
        self.assertEqual(rounded_avg(5, 5), "0b1")
        self.assertEqual(rounded_avg(10, 10), "0b1010")

    def test_rounded_avg_negative(self):
        self.assertEqual(rounded_avg(7, 5), -1)
        self.assertEqual(rounded_avg(20, 15), -1)
        self.assertEqual(rounded_avg(33, 20), -1)
        self.assertEqual(rounded_avg(5, 1), -1)

    def test_rounded_avg_edge_cases(self):
        self.assertEqual(rounded_avg(1, 1), "0b1")
        self.assertEqual(rounded_avg(2, 2), "0b10")
        self.assertEqual(rounded_avg(3, 3), "0b11")
        self.assertEqual(rounded_avg(4, 4), "0b100")

    def test_rounded_avg_invalid_input(self):
        with self.assertRaises(TypeError):
            rounded_avg("a", 5)
        with self.assertRaises(TypeError):
            rounded_avg(1, "b")
        with self.assertRaises(TypeError):
            rounded_avg(1, 5.5)

if __name__ == '__main__':
    unittest.main()


This test suite covers various test cases including positive integers, negative integers, edge cases, and invalid inputs. The test cases are divided into four categories: `test_rounded_avg_positive`, `test_rounded_avg_negative`, `test_rounded_avg_edge_cases`, and `test_rounded_avg_invalid_input`. Each test case checks the output of the `rounded_avg` function against the expected output.