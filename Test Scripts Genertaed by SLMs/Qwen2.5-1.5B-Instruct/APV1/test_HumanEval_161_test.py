system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
You are an expert Python programmer.
Your task is to write a comprehensive unittest test suite for the given Python function.

### Output Formatting
1. Start with: import unittest
2. Include: from HumanEval_161_code import solve
3. End with:
if __name__ == '__main__':
    unittest.main()

Function:
def solve(s):
    """
    You are given a string s.
    - If s[i] is a letter, reverse its case (lower <-> upper).
    - Otherwise, keep it as it is.
    - If the string contains no letters, reverse the string entirely.

    Examples:
        solve("1234") -> "4321"
        solve("ab")   -> "AB"
        solve("#a@C") -> "#A@c"
    """
    flg = 0
    new_str = []

    for i in s:
        if i.isalpha():
            new_str.append(i.swapcase())
            flg = 1
        else:
            new_str.append(i)

    result = "".join(new_str)
    if flg == 0:
        return result[::-1]
    return result


assistant

import unittest

# Function to be tested
from HumanEval_161_code import solve

class TestSolve(unittest.TestCase):

    def test_solve(self):
        self.assertEqual(solve("1234"), "4321")
        self.assertEqual(solve("ab"), "AB")
        self.assertEqual(solve("#a@C"), "#A@c")

    def test_no_letters(self):
        self.assertEqual(solve(""), "")

if __name__ == '__main__':
    unittest.main()


This code snippet defines a `unittest` test suite for the `solve` function. It includes three test cases covering different scenarios where the function behaves as expected and one scenario where there are no letters in the input string. The `test_no_letters` method tests the case when the input string does not contain any alphabetic characters.