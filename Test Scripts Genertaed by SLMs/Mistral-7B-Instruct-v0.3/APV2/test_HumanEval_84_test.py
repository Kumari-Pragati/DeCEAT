You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.

Write a complete unittest test suite for the following Python function.
Follow all rules carefully.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_84_code import solve
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.

    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".

    Variables:
        @N integer
            Constraints: 0 ≤ N ≤ 10000.
    Output:
        a string of binary number
    """

    return bin(sum(int(i) for i in str(N)))[2:]

 Here is the complete unittest test suite for the given Python function `solve()`. I've followed the formatting rules you've provided.


import unittest
from HumanEval_84_code import solve

class TestSolve(unittest.TestCase):

    def test_solve_positive_integer(self):
        test_cases = [
            (1000, "1"),
            (150, "110"),
            (147, "1100"),
            (10, "1"),
            (255, "1111011"),
            (10000, "1001001")
        ]

        for n, expected_result in test_cases:
            with self.subTest(f"Test for N = {n}"):
                self.assertEqual(solve(n), expected_result)

    def test_solve_zero(self):
        self.assertEqual(solve(0), "0")

    def test_solve_negative_integer(self):
        self.assertRaises(ValueError, solve, -1)

if __name__ == '__main__':
    unittest.main()


This test suite includes three test cases:

1. `test_solve_positive_integer` checks the function with positive integers.
2. `test_solve_zero` checks the function with zero.
3. `test_solve_negative_integer` checks if the function raises a ValueError when given a negative integer.