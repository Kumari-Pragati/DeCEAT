system
You are Qwen, created by Alibaba Cloud. You are a helpful assistant.
user
Generate a unittest test script for the following Python function.
The script should fully test the function and be runnable directly.

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

# Test cases to verify the correctness of the 'solve' function
class TestSolve(unittest.TestCase):

    def test_solved(self):
        self.assertEqual(solve("1234"), "4321")
        self.assertEqual(solve("ab"), "AB")
        self.assertEqual(solve("#a@C"), "#A@c")

    def test_empty_string(self):
        self.assertEqual(solve(""), "")

    def test_no_letters(self):
        self.assertEqual(solve("1!2$3%"), "!2$3%")


if __name__ == '__main__':
    unittest.main()


This code snippet defines a `unittest` test class named `TestSolve`. It includes several test methods (`test_solved`, `test_empty_string`, and `test_no_letters`) that call the `solve` function with different inputs and compare the results against expected outputs using assertions. The `unittest.main()` at the end runs all the defined tests when this script is executed.