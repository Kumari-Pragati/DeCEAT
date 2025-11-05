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

 Here is a unittest test script for the provided function `solve()`. I've included several test cases to cover various scenarios.


import unittest
from HumanEval_161_code import solve

class TestSolveFunction(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(solve(""), "")

    def test_only_numbers(self):
        self.assertEqual(solve("1234"), "4321")

    def test_only_letters(self):
        self.assertEqual(solve("ab"), "AB")

    def test_mixed_case_letters(self):
        self.assertEqual(solve("AbCdEf"), "aBcD eF")

    def test_special_characters(self):
        self.assertEqual(solve("#a@C"), "#A@c")

    def test_only_special_characters(self):
        self.assertEqual(solve("!@#$%^&*()"), "*&^%$#@!")

    def test_no_letters_or_numbers(self):
        self.assertEqual(solve(" _-+."), "_-+.")

    def test_leading_trailing_spaces(self):
        self.assertEqual(solve("   ab   "), "   AB   ")

if __name__ == '__main__':
    unittest.main()


This test script includes tests for an empty string, only numbers, only letters, mixed case letters, special characters, no letters or numbers, and leading/trailing spaces. You can run this script directly to test the `solve()` function.