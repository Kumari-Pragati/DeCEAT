You are an AI programming assistant, utilizing the Deepseek Coder model, developed by Deepseek Company, and you only answer questions related to computer science. For politically sensitive questions, security and privacy issues, and other non-computer science questions, you will refuse to answer
### Instruction:
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


### Response:
Here is a unittest script for the given Python function:


import unittest
from HumanEval_84_code import solve

class TestSolve(unittest.TestCase):
    def test_solve(self):
        self.assertEqual(solve(1000), "1")
        self.assertEqual(solve(150), "110")
        self.assertEqual(solve(147), "1100")
        self.assertEqual(solve(0), "0")
        self.assertEqual(solve(1023), "111111")
        self.assertEqual(solve(500), "101")
        self.assertEqual(solve(999), "1111111")

if __name__ == '__main__':
    unittest.main()


This script creates a test case for the `solve` function with several test cases. Each test case checks if the function's output matches the expected output. If all test cases pass, the function is working correctly.

Please note that you need to have the `HumanEval_84_code` module with the `solve` function defined in it for this script to work.

You can run this script directly in a Python environment. If all test cases pass, it will indicate that the `solve` function is working correctly. If any test case fails, it will print out the error message indicating which test case failed and why.