You are an expert Python programmer. 
Your task is to write a comprehensive unittest test suite for the given Python function.

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

 import unittest
from HumanEval_84_code import solve

class TestSolveFunction(unittest.TestCase):

    def test_sum_of_digits_in_binary(self):
        # Test case 1: N = 1000
        self.assertEqual(solve(1000), "1")

        # Test case 2: N = 150
        self.assertEqual(solve(150), "110")

        # Test case 3: N = 147
        self.assertEqual(solve(147), "1100")

        # Test case 4: N = 0
        self.assertEqual(solve(0), "0")

        # Test case 5: N = 10000
        self.assertEqual(solve(10000), "10011")

        # Test case 6: N = 9999
        self.assertEqual(solve(9999), "11111")

        # Test case 7: N = 999
        self.assertEqual(solve(999), "1111")

        # Test case 8: N = 12345
        self.assertEqual(solve(12345), "11000101100")

        # Test case 9: N = 987654321
        self.assertEqual(solve(987654321), "11110111001100010011")

        # Test case 10: N = 999999999
        self.assertEqual(solve(999999999), "11110111001100010011")

        # Test case 11: N = 9999999999
        self.assertEqual(solve(9999999999), "11110111001100010011")

        # Test case 12: N = 99999999999
        self.assertEqual(solve(99999999999), "11110111001100010011")

        # Test case 13: N = 999999999999
        self.assertEqual(solve(999999999999), "11110111001100010011")

        # Test case 14: N = 9999999999999
        self.assertEqual(solve(9999999999999), "11110111001100010011")

        # Test case 15: N = 99999999999999
        self.assertEqual(solve(99999999999999), "11110111001100010011")

if __name__ == '__main__':
    unittest.main()