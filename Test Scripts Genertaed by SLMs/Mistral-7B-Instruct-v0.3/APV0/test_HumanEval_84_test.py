Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

 Here is a unittest test script for the given function `solve()`. I've included test cases for various inputs to ensure the function works correctly.


import unittest
from HumanEval_84_code import solve

class TestSolveFunction(unittest.TestCase):

    def test_solve_with_small_numbers(self):
        self.assertEqual(solve(1), "1")
        self.assertEqual(solve(2), "1")
        self.assertEqual(solve(3), "1")
        self.assertEqual(solve(4), "100")
        self.assertEqual(solve(5), "101")
        self.assertEqual(solve(6), "110")
        self.assertEqual(solve(7), "111")
        self.assertEqual(solve(8), "1000")
        self.assertEqual(solve(9), "1001")
        self.assertEqual(solve(10), "1010")
        self.assertEqual(solve(11), "1011")
        self.assertEqual(solve(12), "1100")
        self.assertEqual(solve(13), "1101")
        self.assertEqual(solve(14), "1110")
        self.assertEqual(solve(15), "1111")

    def test_solve_with_large_numbers(self):
        self.assertEqual(solve(1000), "1")
        self.assertEqual(solve(150), "110")
        self.assertEqual(solve(147), "1100")
        self.assertEqual(solve(10000), "100010")

if __name__ == '__main__':
    unittest.main()


This test script includes two test functions: `test_solve_with_small_numbers` and `test_solve_with_large_numbers`. The former tests the function with small numbers from 1 to 15, and the latter tests the function with larger numbers, including the maximum input of 10000.