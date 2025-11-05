user

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

    return bin(sum(int(i) for i in str(N)))[2:]assistant

Here is the unittest test script for the given Python function:

Python
import unittest
from HumanEval_84_code import solve

class TestSolveFunction(unittest.TestCase):

    def test_solved(self):
        self.assertEqual(solve(1000), "1")
        self.assertEqual(solve(150), "110")
        self.assertEqual(solve(147), "1100")
        self.assertEqual(solve(10000), "11110")
        self.assertEqual(solve(1), "1")
        self.assertEqual(solve(2), "10")
        self.assertEqual(solve(3), "11")
        self.assertEqual(solve(4), "100")
        self.assertEqual(solve(5), "101")
        self.assertEqual(solve(6), "110")
        self.assertEqual(solve(7), "111")
        self.assertEqual(solve(8), "1000")
        self.assertEqual(solve(9), "1001")
        self.assertEqual(solve(10), "1010")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            solve(-1)
        with self.assertRaises(TypeError):
            solve(10001)

if __name__ == '__main__':
    unittest.main()


This script includes two test cases: `test_solved` and `test_invalid_input`. The `test_solved` test case checks the function with valid inputs and compares the output with the expected output. The `test_invalid_input` test case checks the function with invalid inputs (negative number and number greater than 10000) and checks if the function raises a TypeError as expected.