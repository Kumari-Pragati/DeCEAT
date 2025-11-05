You are an expert Python programmer whose primary role is to write comprehensive unittest test suites. Be professional, precise, and output only runnable Python code.### Instruction:
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


### Response:
Here is a unittest test suite for the given Python function:


import unittest
from HumanEval_84_code import solve

class TestSolve(unittest.TestCase):

    def test_solve_positive_integers(self):
        self.assertEqual(solve(1000), "1")
        self.assertEqual(solve(150), "110")
        self.assertEqual(solve(147), "1100")

    def test_solve_zero(self):
        self.assertEqual(solve(0), "0")

    def test_solve_large_numbers(self):
        self.assertEqual(solve(10000), "1")

    def test_solve_constraints(self):
        with self.assertRaises(AssertionError):
            solve(-1)
        with self.assertRaises(AssertionError):
            solve(10001)

if __name__ == '__main__':
    unittest.main()


This test suite includes tests for positive integers, zero, large numbers, and the constraints of the function. It checks if the function returns the correct binary string for each input. It also checks if the function raises an AssertionError when the input is outside the constraints.